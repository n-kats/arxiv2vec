cd `dirname $0`/..
OUTPUT=./_fukaya/dl
mkdir -p $OUTPUT

./bin/downloader \
  -cat math.GT \
  -outputDir $OUTPUT

./bin/downloader \
  -cat math.SG \
  -outputDir $OUTPUT

./bin/downloader \
  -cat math.DG \
  -outputDir $OUTPUT
