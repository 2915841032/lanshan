# FastAPI实现DSR端点
from fastapi import APIRouter

router = APIRouter()

@router.post("/export-data")
async def export_user_data(request: DataExportRequest):
    validator = GDPRValidator(request.user_id)
    if not validator.check_identity(request.auth_token):
        return {"error": "身份验证失败"}
    exporter = DataExporter(request.format)
    return exporter.generate_zip(request.user_id)

@router.delete("/erase-data")
async def erase_user_data(request: DataEraseRequest):
    eraser = DataEraser()
    task_id = eraser.create_erase_task(
        user_id=request.user_id,
        erase_scope=request.scopes
    )
    return {"task_id": task_id, "status_url": f"/tasks/{task_id}"}
