cd `dirname $0`/..

mkdir -p _fukaya/inputs
rm _fukaya/inputs/*

python _fukaya/listup.py \
  --json ./_fukaya/data_gt_sg_dg_20171208.json \
  --output_summary ./_fukaya/summary_list.txt \
  --output_summary_dir ./_fukaya/inputs \
  --output_id ./_fukaya/id_list.txt \
  --output_title ./_fukaya/title_list.txt \
  --target "Fukaya"

python -m cli.main infer \
  output_vectors \
  --input_texts `find ./_fukaya/inputs/input*` \
  --load_model ./_fukaya/model_gt_sg_dg_20171208.pkl \
  --train_data ./_fukaya/data_gt_sg_dg_20171208.txt \
  --output_npz ./_fukaya/output_vecs.npz


