from fastapi import FastAPI, Depends, UploadFile, File, Form, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
import pandas as pd
import io

from models import Interaction,  Metric
from schemas import Interactions
from database import get_db

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Hello"}

@app.get("/interactions")
async def list_interactions(db: Session = Depends(get_db)):
    return db.query(Interaction).all()

@app.get("/metrics")
async def get_metrics(interaction: int = None, db: Session = Depends(get_db)):
    if interaction:
        metrics = db.query(Metric).filter(Metric.log_id==interaction).all()
    else:
        metrics = db.query(Metric).all()
    return metrics

@app.post("/interactions")
async def create_interaction(Interactions: Interactions, db: Session = Depends(get_db)):
    interaction = Interaction(id=Interactions.id,
                              input=Interactions.input,
                              output=Interactions.output)
    input_metric_alert = ""
    output_metric_alert = ""
    if len(Interactions.input) > Interactions.metric:
        input_metric_alert ="Input Length is More than Metric"
    elif len(Interactions.input) < Interactions.metric:
        input_metric_alert = "Input Length is Less than Metric"
    else:
        input_metric_alert = "Length is equal"

    if len(Interactions.output) > Interactions.metric:
        output_metric_alert ="Input Length is More than Metric"
    elif len(Interactions.output) < Interactions.metric:
        output_metric_alert = "Input Length is Less than Metric"
    else:
        output_metric_alert = "Length is equal"

    metric = Metric(log_id=Interactions.id,
                    metric = Interactions.metric,
                    input_metric_alert=input_metric_alert,
                    output_metric_alert=output_metric_alert
                    )
    db.add(interaction)
    db.add(metric)
    db.commit()
    return interaction

async def process_interactions(data: List, metric_length:int, db: Session):
    for interaction in data:
        print(interaction)
        db_interaction = Interaction(id=interaction['id'], input=interaction['input'], output=interaction['output'])
        db.add(db_interaction)
        input_metric_alert = ""
        output_metric_alert = ""

        if len(interaction['input']) > metric_length:
            input_metric_alert = "Input Length is More than Metric"
        elif len(interaction['input']) < metric_length:
            input_metric_alert = "Input Length is Less than Metric"
        else:
            input_metric_alert = "Length is equal"

        if len(interaction['output']) > metric_length:
            output_metric_alert = "Input Length is More than Metric"
        elif len(interaction['output']) < metric_length:
            output_metric_alert = "Input Length is Less than Metric"
        else:
            output_metric_alert = "Length is equal"

        metric = Metric(log_id=db_interaction.id,
                        metric=metric_length,
                        input_metric_alert=input_metric_alert,
                        output_metric_alert=output_metric_alert
                        )
        db.add(metric)
        db.commit()
    return data

@app.post("/upload-interactions")
async def upload_interactions(background_tasks: BackgroundTasks,
                              file: UploadFile = File(...),
                              metric_length: int = Form(...),
                              db: Session = Depends(get_db)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    try:
        contents = await file.read()
        data = pd.read_csv(io.BytesIO(contents)).to_dict(orient='records')
        background_tasks.add_task(process_interactions, data, metric_length, db)
        return {"message":"File uploaded for processing"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

async def delete_log(db: Session = Depends(get_db)):
    db_logs = db.query(Interaction).all()
    for log in db_logs:
        db.delete(log)
    metrics = db.query(Metric).all()
    for metric in metrics:
        db.delete(metric)
    db.commit()
    return db_logs
