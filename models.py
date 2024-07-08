from sqlalchemy import Column, Integer, String, Text, ForeignKey, BigInteger, Sequence
from database import Base


class Interaction(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    input = Column(Text)
    output = Column(Text)

class Metric(Base):
    __tablename__ = "metrics"
    id = Column(BigInteger,Sequence('metrics_id_seq'), primary_key=True, index=True)
    metric = Column(Integer,nullable=True)
    log_id = Column(Integer, ForeignKey(Interaction.id), index=True)
    input_metric_alert = Column(Text)
    output_metric_alert = Column(Text)