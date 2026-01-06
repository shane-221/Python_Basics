import pandas as pd





class CompanyWebsiteSection:
    def __init__(self, **kwargs):
        self.stock =kwargs ["stock"]
        self.price_change = kwargs["price_change"]
        self.articles = kwargs["articles"]
        self.company_name= kwargs["company_name"]


    def structure (self):
        articles_html = ""
        for a in self.articles:
            articles_html += (f"<div class='article'>"
                              f"<a href= {a[3]}>"
                              f"•{a[0]} — {a[1]} — {a[2]}")

        return f"""
            <div class="divider"></div>
            
            <div class="section">
            
                <div class="stock-name">
                    <a href="{"https://blog.recast.ai/module-faster-shadow"}" style="text-decoration:none; color:#3498DB;">
                        {self.company_name} ({self.stock})
                    </a>
                </div>
            
                <div class="price">Price change: {self.price_change}</div>
            
                <div class="divider"></div>
            
                <div class="heading">Articles:</div>
            
                {articles_html}
            
            </div>
            
            <div class="divider"></div>
"""



