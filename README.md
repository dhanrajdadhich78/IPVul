# IPVulnerability Scanner

## About

IP Vulnerability Scanner (IPVul) is a tool made for reconnaissance and information gathering with an emphasis on simplicity.<br> It will do everything from
fetching DNS records, retrieving WHOIS information, obtaining TLS data, detecting WAF presence and up to threaded dir busting and
subdomain enumeration. Every scan outputs to a corresponding file. <br/>

As most of IPVul's scans are independent and do not rely on each other's results,
it utilizes Python's asyncio to run most scans asynchronously. <br/>

IPVul supports Tor/proxy for anonymous routing. It uses default wordlists (for URL fuzzing and subdomain discovery)
from the amazing [SecLists](https://github.com/danielmiessler/SecLists) repository but different lists can be passed as arguments.<br>

For more options - see "Usage".

## Features

- [x] DNS details
- [x] DNS visual mapping using DNS dumpster
- [x] WHOIS information
- [x] TLS Data - supported ciphers, TLS versions,
certificate details and SANs
- [x] Port Scan
- [x] Services and scripts scan
- [x] URL fuzzing and dir/file detection
- [x] Subdomain enumeration - uses Google dorking, DNS dumpster queries,
 SAN discovery and bruteforce
- [x] Web application data retrieval:<br>
  - CMS detection
  - Web server info and X-Powered-By
  - robots.txt and sitemap extraction
  - Cookie inspection
  - Extracts all fuzzable URLs
  - Discovers HTML forms
  - Retrieves all Email addresses
  - Scans target for vulnerable S3 buckets and enumerates them
  for sensitive files
- [x] Detects known WAFs
- [x] Supports anonymous routing through Tor/Proxies
- [x] Uses asyncio for improved performance
- [x] Saves output to files - separates targets by folders
and modules by files

## Installation

To run the code:

``` sh
cd IPVul
python setup.py install # Subsequent changes to the source code will not be reflected in calls to ipvul when this is used
```

## Or

python setup.py develop # Changes to code will be reflected in calls to ipvul. This can be undone by using python setup.py develop --uninstall

## Finally

``` sh
ipvul [OPTIONS] [TARGET]
```

## macOS

To support IPVul on macOS you need to have gtimeout on your machine.<br>
gtimeout can be installed by running `brew install coreutils`.

## Docker

``` sh
# Build the docker image

docker build -t dhanrajdadhich78/ipvul .

# Run a scan, As this a non-root container we need to save the output under the user's home which is /home/ipvul

docker run --name ipvul dhanrajdadhich78/ipvul:latest  example.com -o /home/ipvul

```

## Prerequisites

IPVul uses [Nmap](https://github.com/nmap/nmap) to scan ports as well as utilizes some other Nmap scripts
and features. It is mandatory that you have it installed before running IPVul.<br>
[OpenSSL](https://github.com/openssl/openssl) is also used for TLS/SSL scans and should be installed as well.

## Usage

``` text

Usage: ipvul [OPTIONS] TARGET

Options:
  --version                      Show the version and exit.
  -d, --dns-records TEXT         Comma separated DNS records to query.
                                 Defaults to: A,MX,NS,CNAME,SOA,TXT
  --tor-routing                  Route HTTP traffic through Tor (uses port
                                 9050). Slows total runtime significantly
  --proxy-list TEXT              Path to proxy list file that would be used
                                 for routing HTTP traffic. A proxy from the
                                 list will be chosen at random for each
                                 request. Slows total runtime
  -c, --cookies TEXT             Comma separated cookies to add to the
                                 requests. Should be in the form of key:value
                                 Example: PHPSESSID:12345,isMobile:false
  --proxy TEXT                   Proxy address to route HTTP traffic through.
                                 Slows total runtime
  -w, --wordlist TEXT            Path to wordlist that would be used for URL
                                 fuzzing
  -T, --threads INTEGER          Number of threads to use for URL
                                 Fuzzing/Subdomain enumeration. Default: 25
  --ignored-response-codes TEXT  Comma separated list of HTTP status code to
                                 ignore for fuzzing. Defaults to:
                                 302,400,401,402,403,404,503,504
  --subdomain-list TEXT          Path to subdomain list file that would be
                                 used for enumeration
  -sc, --scripts                 Run Nmap scan with -sC flag
  -sv, --services                Run Nmap scan with -sV flag
  -f, --full-scan                Run Nmap scan with both -sV and -sC
  -p, --port TEXT                Use this port range for Nmap scan instead of
                                 the default
  --vulners-nmap-scan            Perform an NmapVulners scan. Runs instead of
                                 the regular Nmap scan and is longer.
  --vulners-path TEXT            Path to the custom nmap_vulners.nse script.If
                                 not used, IPVul uses the built-in script it
                                 ships with.
  -fr, --follow-redirects        Follow redirects when fuzzing. Default: False
                                 (will not follow redirects)
  --tls-port INTEGER             Use this port for TLS queries. Default: 443
  --skip-health-check            Do not test for target host availability
  --no-url-fuzzing               Do not fuzz URLs
  --no-sub-enum                  Do not bruteforce subdomains
  --skip-nmap-scan               Do not perform an Nmap scan
  -q, --quiet                    Do not output to stdout
  -o, --outdir TEXT              Directory destination for scan output
  --help                         Show this message and exit.

```

## Screenshots

![poc2](https://github.com/dhanrajdadhich78/IPVul/tree/main/output/response1.png)<br>

**Web application data including vulnerable S3 bucket:**<br>
![somepoc](https://github.com/dhanrajdadhich78/IPVul/tree/main/output/response2.png)

**[HTB](https://www.hackthebox.eu/) challenge example scan:**<br>
![poc](https://github.com/dhanrajdadhich78/IPVul/tree/main/output/response3.png)<br>

**Nmap vulners scan results:**<br>
![vulnerspoc](https://github.com/dhanrajdadhich78/IPVul/tree/main/output/response4.png)<br>

**Results folder tree after a scan:**<br>
![poc3](https://github.com/dhanrajdadhich78/IPVul/tree/main/output/response5.png)
