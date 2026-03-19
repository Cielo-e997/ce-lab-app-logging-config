import logging
import json
import uuid
from flask import Flask, request, jsonify

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "event": record.getMessage(),
            "level": record.levelname.lower(),
            "timestamp": self.formatTime(record, self.datefmt)
        }

        if hasattr(record, "extra_fields"):
            log_record.update(record.extra_fields)

        return json.dumps(log_record)

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("/home/ubuntu/ce-lab-app-logging-config/app/application.log")
file_handler.setFormatter(JsonFormatter())

console_handler = logging.StreamHandler()
console_handler.setFormatter(JsonFormatter())

logger.addHandler(file_handler)
logger.addHandler(console_handler)

app = Flask(__name__)

@app.route('/')
def index():
    correlation_id = request.headers.get('X-Correlation-ID', str(uuid.uuid4()))

    logger.info(
        "request_received",
        extra={
            "extra_fields": {
                "correlation_id": correlation_id,
                "path": "/",
                "method": request.method,
                "ip": request.remote_addr
            }
        }
    )

    return jsonify({
        "message": "Hello World",
        "correlation_id": correlation_id
    })

@app.route('/health')
def health():
    logger.info(
        "health_check",
        extra={
            "extra_fields": {
                "status": "healthy"
            }
        }
    )

    return jsonify({"status": "healthy"})

@app.route('/order', methods=['POST'])
def create_order():
    correlation_id = str(uuid.uuid4())
    data = request.get_json(silent=True) or {}

    logger.info(
        "order_created",
        extra={
            "extra_fields": {
                "correlation_id": correlation_id,
                "order_id": f"ord-{uuid.uuid4().hex[:8]}",
                "amount": data.get("amount", 0),
                "items": data.get("items", 0),
                "user_id": data.get("user_id")
            }
        }
    )

    return jsonify({
        "status": "created",
        "correlation_id": correlation_id
    })

if __name__ == '__main__':
    logger.info(
        "application_started",
        extra={
            "extra_fields": {
                "port": 5000
            }
        }
    )
    app.run(host='0.0.0.0', port=5000)
