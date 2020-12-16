#!/bin/bash
aws s3 cp data/dividends.json s3://"$BUCKET_NAME"
