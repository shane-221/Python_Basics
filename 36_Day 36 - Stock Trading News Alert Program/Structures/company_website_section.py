class CompanyWebsiteSection:
    def __init__(self, **kwargs):
        self.stock =kwargs ["stock"]
        self.price_change = kwargs["price_change"]
        self.articles = kwargs["articles"]
        self.article_number=-1

    def structure (self):
        articles_html = ""
        for a in self.articles:
            articles_html += f"<mj-text>{a[0]} -- {a[1]} -- {a[2]}</mj-text>\n"

        return f"""
                <mj-section>
      <mj-column width="75%">
        <mj-text>
          <h3 style="font-weight: bold; margin-top: 0; margin-bottom: 0"> <a href="https://blog.recast.ai/module-faster-shadow/" style="color: #3498DB; text-decoration: none">
              {self.stock}
            </a> </h3>
          <p style="font-size: 14px"> Price change: {self.price_change}</p>
        </mj-text>
      </mj-column>
      <mj-column width="25%">
        <mj-text font-size="14px" line-height="1.4">
                    {articles_html}
   			</mj-text>
      </mj-column>
    </mj-section>
        """
