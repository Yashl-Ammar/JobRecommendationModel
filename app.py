from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load data
df2 = pd.read_csv('freelancer_job_postings.csv', index_col='projectId')
df = df2.dropna()

# Compute cosine similarity matrix
count2 = CountVectorizer(stop_words='english', lowercase=True)
count_matrix2 = count2.fit_transform(df2['job_title'])
cosine_sim2 = cosine_similarity(count_matrix2, count_matrix2)
cosine_sim_df2 = pd.DataFrame(cosine_sim2)


def content_recommendation_v2(title):
    a = df2.copy().reset_index().drop('projectId', axis=1)
    index = a[a['job_title'] == title].index[0]

    # Use cosine_sim_df2 instead of cosine_sim_df
    similar_basis_metric_1 = cosine_sim_df2[cosine_sim_df2[index] > 0][index].reset_index().rename(
        columns={index: 'sim_1'})

    # Continue with cosine_sim_df2
    similar_basis_metric_2 = cosine_sim_df2[cosine_sim_df2[index] > 0][index].reset_index().rename(
        columns={index: 'sim_2'})

    similar_df = similar_basis_metric_1.merge(similar_basis_metric_2, how='left').merge(
        a[['job_description']].reset_index(), how='left')
    similar_df['sim'] = similar_df[['sim_1', 'sim_2']].fillna(0).mean(axis=1)
    similar_df = similar_df[similar_df['index'] != index].sort_values(by='sim', ascending=False)
    return similar_df[['job_description', 'sim']].head(60)


@app.route('/recommendation', methods=['POST'])
def recommendation():
    data = request.get_json()
    title = data['title']
    recommended_jobs = content_recommendation_v2(title)
    return jsonify(recommended_jobs.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
