# Postmortem

![car hitting an egg](incident.jpg)

## Issue Summary

We had just launched a new feature for Rhojees Online Shoe Shop web app. After a few hours, the first intake of users started complaining about the site. We recieved several emails from who complained that "they can't sign in or sign up to the platform".

It was quite surprising to us because we knew it worked on our machines and it worked before. We recieved over 200 emails from other users who were experiencing the same problem, and we knew that we had to do something quickly.

Knowing how hard it can be to attract and keep users, we couldn't afford to losemore than 200 of their users. So, we decided to take a closer look at the problem.

First, we cloned our site's repository from GitBug, followed the installation instructions on the README and to our surprise the site couldn't startup. It wasn't long before we realized that the cause of the problem was failing to update the requirements for our project. The site was malfunctioning from 9:55 AM EAT, when we deployed the new feature until 14:12 AM EAT when we fixed the issue.

## Timeline

+ 12-02-2024 9:55 AM EAT - The first customer complained that they couldn't sign in to the site.
+ 12-02-2024 11:20 AM EAT - One of our backend developers, Linus, experienced the same issues that our customers reported.
+ 12-02-2024 11:45 AM EAT - We investigated the controllers and the views for inconsistencies.
+ 12-02-2024 11:53 AM EAT - We assumed the bcrypt (one of our site's dependencies) gem being used was either at fault or used incorrectly because the error message on the site showed that the bcrypt gem was raising an error over an invalid hash.
+ 12-02-2024 12:42 PM EAT - We checked that the views might not be binding the form fields to the right model fields, which later turned out to be false.
+ 12-02-2024 13:05 PM EAT - We were misled by thinking that our controllers might be creating a different hash for a valid password of the site's admin.
+ 12-02-2024 13:35 PM EAT - Winus thought the issue might have been that the password was not properly hashed.
+ 12-02-2024 14:00 PM EAT - The incident was escalated to the backend development team.
+ 12-02-2024 14:12 PM EAT - The incident was resolved by updating the requirements (the bcrypt gem version) for the backend server.

## Root Cause And Resolution

The version of the bcrypt gem we used was outdated. It was raising an error over a hash that was clearly valid and matched what was stored in the database. It could be that the hash we were creating was not supported by the version of bcrypt we had installed. Winus fixed the issue by manually updating the version of bcrypt in the Gemfile.lock file to a more recent version and reinstalling the required gems, and it worked like a charm.

## Corrective And Preventative Measures

+ Setup a continuous integration pipeline to run a build on each pull request branch. This would ensure that builds are passing in the pull request branch before it is merged with the deployment branch.
+ Setup a monitoring system for the database and application servers to keep track of any issue that may occur.
+ Develop tests that need to be passed for each new feature and those tests should be passing before they are merged with the deployment branch.
