from datetime import datetime, timezone

def build_success_response(message, data=None, extra_meta=None):
    meta = {
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    if extra_meta:
        meta.update(extra_meta)

    response = {
        "success": True,
        "message": message,
        "meta": meta
    }

    if data is not None:
        response["data"] = data

    return response

def build_error_response(message, code, details=None):
    formatted_details = []

    if details:
        for err in details:
            loc = err.get("loc", [])
            field = loc[-1] if loc else "unknown"

            formatted_details.append({
                "field": field,
                "message": err.get("msg", "Invalid value")
            })


    return {
        "success": False,
        "message": message,
        "error": {
            "code": code,
            "details": formatted_details
        },
        "meta": {
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }