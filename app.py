# from flask import Flask, request, jsonify
# from pymongo import MongoClient

# app = Flask(__name__)

# client = MongoClient('mongodb+srv://root:root@cluster0.lhlezvs.mongodb.net/web_wahyunt?retryWrites=true&w=majority')
# db = client['web_wahyunt']
# skills_collection  = db['skills']

# @app.route('/skills', methods=['GET'])
# def get_skills():
#     try:
#         skills = list(skills_collection.find({}, {'_id': 0}))  # Exclude _id
#         return jsonify(skills)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # POST: Tambah skill baru
# @app.route('/skills', methods=['POST'])
# def add_skill():
#     data = request.json
#     new_skill = {'name': data['name'], 'level': data['level']}
#     skills_collection.insert_one(new_skill)
#     return jsonify(new_skill), 201

# # PUT: Update skill berdasarkan nama
# @app.route('/skills/<string:skill_name>', methods=['PUT'])
# def update_skill(skill_name):
#     data = request.json
#     skills_collection.update_one({'name': skill_name}, {'$set': data})
#     updated_skill = skills_collection.find_one({'name': skill_name}, {'_id': 0})
#     return jsonify(updated_skill)

# # DELETE: Hapus skill berdasarkan nama
# @app.route('/skills/<string:skill_name>', methods=['DELETE'])
# def delete_skill(skill_name):
#     skills_collection.delete_one({'name': skill_name})
#     return '', 204

# if __name__ == '__main__':
#     app.run(debug=True)

print("Hello World")