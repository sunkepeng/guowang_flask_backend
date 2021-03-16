from guowang_backend import app
import json


@app.route('/contest/to_start', methods=['POST'])
def to_start():
    # TODO 启动模型进行图像识别
    return json.dumps({"statusCode": 0, "message": "成功"}, ensure_ascii=False)
    # 失败
    # return json.dumps({"statusCode": 1, "message": "失败"}, ensure_ascii=False)
