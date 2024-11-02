# Sample Codalab

I made this simple example containing
- competition_bundle
- submission_example

In competition_bundle is a zipped version of the main files in that directory. That should work when uploading to codalab.

In submission example is a single file `preds.txt` which contains
```
yes
yes
no
no
yes
```
The scoring script checks this against the file labels.txt in `competition_bundle/reference.zip` which contains:
```
yes
yes
yes
yes
yes
```
and computes accuracy, precision, recall, and f1-score using sklearn functions. These then go into the leaderboard which is set up in `competition.yaml` to handle those 4 outputs.

There are some required .html files in the competition bundle:
- data.html
- overview.html
- evaluation.html
- terms.html
and it's mostly just important that these exist. You can edit them later in codalab anyways.

The main magic happens in `competition_bundle/scoring_script/score.py`. I tried to keep this fairly simple but still contain some kind of evaluation that matches what you might actually want to do for your task, unlike some of the other codalab examples which might be too simple. The main thing to note here is that codalab automatically unzips your submission and reference data into input/res and input/ref, respectively. So when your scoring script looks for these files, make sure to look in those locations.

Feel free to reach out on Discord if you have other questions. Hope this helps!
