from flask import Flask, json

api = Flask(__name__)

@api.route('/text_analyzer', methods=['GET'])
def get_text_analyzed():
  return json.dumps({ "success": True })

if __name__ == '__main__':
    api.run()