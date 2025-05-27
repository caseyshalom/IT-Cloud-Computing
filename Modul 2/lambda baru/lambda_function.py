import json
import base64
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Raw event: %s", json.dumps(event))
    output_records = []
    
    for record in event["records"]:
        try:
            # Decode
            payload = base64.b64decode(record["data"]).decode("utf-8")
            json_data = json.loads(payload)
            
            # Add timestamp (UTC with milliseconds)
            json_data["processedAt"] = (
                datetime.datetime.now(datetime.timezone.utc)
                .isoformat(timespec="milliseconds")
            )
            
            # Prepare output with newline
            json_string = json.dumps(json_data) + "\n"
            b64_encoded_data = base64.b64encode(
                json_string.encode("utf-8")
            ).decode("ascii")
            
            output_records.append({
                "recordId": record["recordId"],
                "result": "Ok",
                "data": b64_encoded_data
            })
            
            logger.info("Processed record: %s", json_data)
            
        except Exception as e:
            logger.error("Processing failed: %s", str(e), exc_info=True)
            output_records.append({
                "recordId": record["recordId"],
                "result": "ProcessingFailed",
                "data": record["data"]
            })
    
    logger.info("Output records: %s", output_records)
    return {"records": output_records}