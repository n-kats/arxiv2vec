cd `dirname $0`/..

python -m cli.main \
  dataset json_arxiv \
  --input `find ./_fukaya/dl/*.json` \
  --output _fukaya/data_gt_sg_dg_20171208.txt

python -m cli.main \
  dataset merge_json \
  --input `find ./_fukaya/dl/*.json` \
  --output _fukaya/data_gt_sg_dg_20171208.json

python -m cli.main \
  train --model doc2vec \
  --preprocess tex \
  --train_data _fukaya/data_gt_sg_dg_20171208.txt \
  --save_model _fukaya/model_gt_sg_dg_20171208.pkl
