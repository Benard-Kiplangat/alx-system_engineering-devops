# 0x0A-configuration managent

Configuration managent is the process of handling system changes systematically to ensure its integrity over time.

In this project, I used puppet to create a file, install a package, and kills a process.

## Task 0: Using Puppet to create a file

Requirements:

- File path is /tmp/school
- File permission is 0744
- File owner is www-data
- File group is www-data
- File contains I love Puppet

### How to run
puppet apply 0-create\_a\_file.pp

## Task 1: Using Puppet, install a package

Requirements:

- Install flask
- Version must be 2.1.0

### How to run

puppet apply 1-install\_a\_package.pp

## Task 2: Using Puppet, create a manifest that runs a executable

Requirements:

- Must use the exec Puppet resource to kill killmenow running process
- Must use pkill

### How to run

puppet apply 2-execute\_a\_command.pp

