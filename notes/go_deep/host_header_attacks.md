# Http HOST Header Attacks
	- Host header is compulsory since HTTP 1.1
	- This Vulnerabilities are occuring due to misconfigurations and very less due to insecure coding practice.
	- This is due to integration of extra applications into websites, like in wix we are integrating different applications.

# How to test host header attacks
	1. We need to identify, whether even after modifying host value are we reaching our target website.
	2. What happens after we change hosts?
		a. Do we get directed to target website? Which means, web application does not recognize the host and by default sends us to  default application...This is where we need to research more.
		b. Do we get invalid host header, that means there is some sort of CDN in between which does not know where to direct you. ... At this point we can test for something else. 
			1. Why do we get Invalid Host header or why our repeater stays in hanging state after manipulation of host header? One of the reason might be because of SNI from TLS Handshake is matched with Host header that we specify.

# Techniques to test for Host Header attacks.
	1. Try to pass port number with hostname, for eg: example.com:80
		a. Application might try to omit the port number, try to include non numeric payload, like some sort of injection ,which will trigger error.
	2. Some might check the host header manually like if it matches example.com
		a. This time, we will register a domain like this anydomain-example.com , application might use wild cards to check if hostname contains example or not?
	3. Specify multiple host header values, frontend might like first one whereas backend might prefer second one.
		a. Foreg: host: target.com ; host: payload.com
	4. Supply an absolute url in GET Request header and payload in host header. Try with different protocol as well, like http and https.
		a. GET http://vulnerable-website.com/ HTTP 1.1 ; host: payload
	5. 

# Questions
	1. What is virtual hosting in detail? and how different websites can have same IP Address?
