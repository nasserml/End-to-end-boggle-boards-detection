from boggleBoardsDetection.logger import logging
from boggleBoardsDetection.exception import AppException
import sys
from boggleBoardsDetection.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()