

class CompanyWebsiteSection:
    def __init__(self, **kwargs):
        self.stock =kwargs ["stock"]
        self.price_change = kwargs["price_change"]
        self.articles = kwargs["articles"]
        self.article_number=-1



    def structure (self):
        articles_html = ""
        for a in self.articles:
            articles_html += (f"<div class='article'>"
                              f"<a href= {a[3]}>"
                              f"•{a[0]} — {a[1]} — {a[2]}")

        return f"""
                <div class="section">
      <!-- Stock name -->
      <div class="stock-name">
        <a href="https://blog.recast.ai/module-faster-shadow/" style="text-decoration:none; color:#3498DB;">
          {self.stock}
        </a>
      </div>

      <!-- Price change -->
      <div class="price">Price change:{self.price_change}</div>

      <!-- Divider -->
      <div class="divider"></div>

      <!-- Articles heading -->
      <div class="heading">Articles:</div>

      <!-- Articles list -->
      {articles_html}
 </div>
       \n """



