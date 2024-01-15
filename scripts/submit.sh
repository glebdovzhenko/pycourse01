if [ ! -d ".git" ]; then
  git init -b "$USER"
  git remote add origin /srv/git/studentlab.git 
  git config user.email "$USER@fake.faux"
  git config user.name "$USER"
fi

if [ ! -f ".gitignore" ]; then
  touch .gitignore
  echo ".gitignore" >> .gitignore
  echo ".ipynb_checkpoints" >> .gitignore
  echo "submit.sh" >> .gitignore
fi

git add . && git commit -m "$(date)" && git push origin $USER

