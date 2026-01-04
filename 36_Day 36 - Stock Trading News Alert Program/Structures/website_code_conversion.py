class CompanyWebsiteSection:
    def __init__(self, **kwargs):
        self.stock =kwargs ["stock"]
        self.price_change = kwargs["price_change"]
        self.articles = kwargs["articles"]
        self.article_number=-1

    def structure (self):
        articles_html = ""
        for a in self.articles:
            articles_html += f"<div class='article'>•{a[0]} — {a[1]} — {a[2]}\n</div>"
        print(articles_html)



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
      <div class="article">• Securityaffairs.com — IBM warns of critical API Connect bug enabling remote access — Pierluigi Paganini</div>
      <div class="article">• BBC News — AI teachers and cybernetics - what could the world look like in 2050? — None</div>
      <div class="article">• Pypi.org — iLibrary 0.0.12 — iLibrary@legner.beer</div>
      <div class="article">• Hootsuite.com — Social media leadership skills enterprise teams needs in 2026 — Colleen Christison</div>
      <div class="article">• Biztoc.com — Melinda French Gates got her start at Microsoft because an IBM hiring manager told her to turn down their job offer — fortune.com</div>
    </div>
        """



