# news-image-20261117-v2

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/AndryXSad/news-image-20261117-v2/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/AndryXSad/news-image-20261117-v2/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A make.fun `news-image-20261117` entry: one image summing up the world's
news of Tuesday, 17 November 2026, as a newspaper front page.

Version 2 rebuilds the page from scratch to widen coverage and make it read
better: 33 stories from six continents, a world map marking 12 places that
made the news, a large Kerch Bridge lead illustration plus three more
illustrated stories (tankers hit in the Strait of Hormuz, the Vulcan rocket
failure, Japan scrambling jets), a nine-story grid, fifteen one-line briefs
from around the world, and a ticker. The page leads with Ukraine bringing
down a span of the Kerch Bridge, then Russia hitting two Kyiv bridges,
Iran's drone attack on Bahrain and the US strike back, Mongolia's president
resigning, Trump in Manila for ASEAN, Nvidia's $115.8bn quarter, the UK
sanctioning eight Israeli firms, the DR Congo Ebola toll, and more. Every
fact on the page was checked against real reporting of that day.

## How it is built

`render.py` (kept outside this repository) drew `entry.png` with PIL from
the verified stories; `main.py` copies that image to `/output/entry.png`.
Standard library only, no network, deterministic — two runs write identical
bytes. The image is 1024x1024 px and under 1 MiB.
