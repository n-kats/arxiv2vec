cd `dirname $0`/..

python ./_fukaya/classify.py \
  --npz ./_fukaya/output_vecs.npz \
  --title ./_fukaya/title_list.txt \
  --id ./_fukaya/id_list.txt
