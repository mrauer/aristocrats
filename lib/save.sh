#!/bin/bash
aws s3 cp data/dividends.json s3://"$BUCKET_NAME"
aws s3 cp data/history.json s3://"$BUCKET_NAME"
