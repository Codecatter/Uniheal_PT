def callback(commit):
    if commit.author_name == b"lovable-dev[bot]":
        commit.author_name = b"Codecatter"
        commit.author_email = b"vijayakatke.312@gmail.com"
    if commit.committer_name == b"lovable-dev[bot]":
        commit.committer_name = b"Codecatter"
        commit.committer_email = b"vijayakatke.312@gmail.com"
