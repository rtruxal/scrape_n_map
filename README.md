## Mappin' Websites!

# What this is supposed to do:

    1. Take a root website as input
    2. Save **request**ed html text to persistent objects in 'prettified' format
        - Design DBMS for a NoSQL Document-like DB (maybe redis...)
        - See step 5. for gemeral DBMS query specifications
    3. Turn our **request** into **soup** and extract & store links from html
        - Additionally, mitigate return of duplicate links for scraping
        - However, while duplicate links are not returned for further navigation processing,
          records of page-relations are still maintained in persistant key-value format
            --ie: {<node> : <corresponding edges>
        - A **Counter** is used to keep track of link-prevalence and to prevent 
          duplicate return during navigation
    4. Handle unpredicted server-response values to allow for 'set-and-forget' automation
    5. Create **re** and **BeautifulSoup** based querying mechanism to access and visualize records/connections
    
# This is what we got so far...
    - Scraper which extracts, stores, and monitors links from html.
    
# Left to do...
    - DBMS (Storage, Querying, and Overall-Format)
    - Exception handling and/or **ANY KIND OF UNIT TESTING AT ALL**    
    