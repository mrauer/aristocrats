#!/bin/bash
aws s3 cp s3://"$BUCKET_NAME"/dividends.json data/
aws s3 cp s3://"$BUCKET_NAME"/history.json data/
