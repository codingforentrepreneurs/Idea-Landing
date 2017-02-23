![Create an Idea Landing Page Logo](https://cfe2-static.s3-us-west-2.amazonaws.com/media/projects/idea-landing/images/share/Idea_Landing_Share.png)

# Create an Idea Landing Page
A rapid-fire building of a dynamic landing page to introduce the series -- HiitStartup \\ [https://kirr.co/kb0y88](https://kirr.co/kb0y88). 

Use this project to launch your idea today. 

Watch here: [https://www.codingforentrepreneurs.com/projects/idea-landing/](https://www.codingforentrepreneurs.com/projects/idea-landing/)


[![Deploy to Heroku Icon](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/codingforentrepreneurs/Idea-Landing/tree/master)

If using a custom domain, go to your Heroku account `https://dashboard.heroku.com/apps/<your-app-name>/settings` then add your custom domain. Ensure this domain is in your `Config Variables` which is also on that page. Restart all dynos if needed.


=====

Launching on your own project:

1. Create & Activate Virtualenv:

    ```
    $ cd ~/desktop
    $ virtualenv -p python 3 knockenv && cd knockenv
    $ source bin/activate
    ```
2. Clone project:

    ```
    $ pwd 
    /desktop/knockenv/
    $ mkdir src && cd src
    $ git clone https://github.com/codingforentrepreneurs/Idea-Landing .
    $ pip install -r requirements.txt
    ```
3. Remove & Start new Git Repo:

    ```
    $ rm -rf .git # removes old git repo
    $ git init # creates your new repo
    $ git add --all
    $ git commit -m "Initial Commit"
    ```

4. Create Heroku App:

    ```
    $ pwd 
    /desktop/knockenv/src/
    $ heroku create
    ```
    In `production.py` add your newly created url such as `https://<yourapp>.herokuapp.com/` to `ALLOWED_HOSTS`. Save `production.py`
    ```
    $ git add --all
    $ git commit -m "Updated production"
    ```
    
5. Add Database & Deploy:

    ```
    $ heroku addons:create heroku-postgresql:hobby-dev
    $ git push heroku master
    $ heroku run python manage.py migrate
    $ heroku run python manage.py createsuperuser
    ```
   
6. Add Custom Domain (optional):
    - Update `production.py`'s `ALLOWED_HOSTS` to include your custom domain such as `ALLOWED_HOSTS = ['.sporproject.com', 'knockhq.herokuapp.com']`
    ```
    $ heroku domains:add *.sporproject.com
    ```
    Update your DNS as needed [here](https://github.com/codingforentrepreneurs/Guides/blob/master/all/Heroku_Django_Deployment_Guide.md#add-custom-domain-name)
