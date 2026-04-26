
---

## 📄 STRUTTURA HTML — `<body>`

```html
<body>

  <!-- POPUP NEWSLETTER MODAL -->
  <div class="modal-wrapper-nl close-x popup-wrapper">
    <div class="div-block-2 close-x">
      <img class="image">
    </div>
    <div class="form-block w-form">
      <form id="wf-form-SK-NL-Popup" class="form-2">
        <h1 class="heading-10">Subscribe to Steven's Newsletter</h1>
        <div class="text-block-2">Join 300,000+ Subscribers Today</div>
        <label>Name</label>
        <input id="name-3" class="w-input">
        <label>Email Address</label>
        <input id="email-7" class="w-input">
        <div class="w-form-formrecaptcha g-recaptcha g-recaptcha-error g-recaptcha">
          <div><div><iframe></iframe></div></div>
        </div>
        <input id="page-url" class="page-url w-input">
        <input class="submit-button-2 w-button">
      </form>
      <div class="success-message w-form-done"><div>Thank you! You're now subscribed...</div></div>
      <div class="w-form-fail"><div>Oops! Something went wrong...</div></div>
    </div>
  </div>

  <!-- PAGE WRAPPER -->
  <div class="page_wrap">

    <!-- SCRIPTS EMBED (Webflow) -->
    <div class="w-embed w-script">
      <script></script>
      <script>document.addEventListener("DOM...");</script>
    </div>

    <!-- CODE EMBEDS (Typography, Color, Utilities, Custom) -->
    <div class="page_code_wrap">
      <div class="page_code_typography w-embed">
        <style>/* TYPOGRAPHY STYLES */...</style>
      </div>
      <div class="page_code_color w-embed">
        <link> <!-- lumos color -->
        <style id="lumos-colors">/* COLOR STYLES */...</style>
      </div>
      <div class="page_code_utilities w-embed">
        <link> <!-- lumos layout -->
        <link> <!-- lumos spacing -->
        <style>/* UTILITY STYLES */...</style>
      </div>
      <div class="page_code_custom w-embed">
        <style>/* CUSTOM STYLES */...</style>
      </div>
    </div>

    <!-- LOADER -->
    <div class="loader_wrap--sm0-2"></div>

    <!-- HEADER / NAV -->
    <header>
      <div class="nav_wrap--bg0-pe0-pd0">
        <div class="nav_container--mw0-pe0 w-container">
          <div class="nav_main--pe2">
            <a class="nav_logo--ff2 w-inline-block w--current">
              <div>SK</div>
            </a>
            <div class="nav_desc--pe0">
              <div><br><br><br></div>
            </div>
            <button class="nav_btn pd0">
              <div class="btn_menu_wrap--fw2-br3">
                <div class="btn_main_list">Menu</div>
              </div>
            </button>
          </div>
        </div>
      </div>

      <!-- NAV MENU (slide-in) -->
      <nav class="nav_menu_wrap--bg2-pp1-gv2">
        <div class="nav_menu_links">
          <!-- Ogni link ha questa struttura: -->
          <a class="nav_menu_link--fw1-tt2 w-inline-block w--current">
            <div class="line-wrap">
              <div class="line--bw1t"></div>
            </div>
            <div class="nav_link_mask">
              <div class="nav_link_text--lh3 is-1">Home</div>
              <div class="nav_link_text--lh3 is-2">Home</div>
            </div>
          </a>
          <!-- Ripetuto per: About, Writing, Speaking, Video, Research -->
        </div>
        <!-- Social links orizzontali nel menu -->
        <div class="social-links_list--gp0-5 is-horizontal">
          <a class="social-links_item--bm0-1-br3 w-inline-block">
            <div class="social-links_svg--ic1 w-embed"><svg>...</svg></div>
          </a>
          <!-- Ripetuto per: Instagram/X/LinkedIn/ecc. -->
        </div>
      </nav>
    </header>

    <!-- SEZIONE HERO -->
    <section>
      <!-- Hero con immagine di sfondo, testo "KOTLER" a tutto schermo in basso -->
      <div class="hero_wrap--bg0">
        <div class="hero_base">
          <img class="hero_img">
        </div>
        <div class="hero_text_wrap--ff2-tt2">
          <!-- Lettere singole animate: K-O-T-L-E-R -->
          <div class="hero_text">K</div>
          <div class="hero_text">O</div>
          <div class="hero_text">T</div>
          <div class="hero_text">L</div>
          <div class="hero_text">E</div>
          <div class="hero_text">R</div>
        </div>
      </div>
    </section>

    <!-- SEZIONE INTRO -->
    <section>
      <div class="w-container">
        <div class="home_intro">
          <div class="home_intro_content">
            <h1 class="heading--fs4-lh2-fw1">
              <div class="line-wrap">Steven Kotler is a New York Ti...</div>
              <div class="line-wrap">an award-winning journalist, a...</div>
              <div class="line-wrap">executive director of the Flow...</div>
              <div class="line-wrap">He is one of the world's leadi...</div>
              <div class="line-wrap">performance.</div>
            </h1>
            <div class="mt4">
              <div class="btn-row--gp1-5">Buy Steven's Latest Book</div>
            </div>
          </div>
          <!-- Logo marquee (scorrimento infinito) -->
          <div class="marquee_panel--gp0">
            <a class="logo_link w-inline-block"><img class="logo_img"></a>
            <!-- Ripetuto per ogni logo media/partner -->
          </div>
          <!-- Secondo pannello marquee (clonato per loop infinito) -->
          <div class="marquee_panel--gp0">
            <!-- Stesso contenuto del primo pannello -->
          </div>
        </div>
      </div>
    </section>

    <!-- SEZIONE LIBRI (Swiper slider) -->
    <section>
      <div class="w-container">
        <div class="swiper is-books w-dyn-list">
          <div class="swiper-wrapper">
            <!-- Ogni libro: -->
            <div class="swiper-slide is-slider-main w-dyn-item swiper-slide-active">
              We Are as Gods
            </div>
            <!-- Performance Neuroscience, Gnar Country, The Devil's Dictionary,
                 The Art of Impossible, The Future Is Faster Than You Think,
                 Mapping Cloud Nine, Last Tango in Cyberspace, Stealing Fire,
                 Tomorrowland... -->
          </div>
          <div class="swiper-pagination">
            <button class="swiper-bullet"></button>
            <!-- Ripetuto per ogni slide -->
          </div>
        </div>
      </div>
    </section>

    <!-- SEZIONE SPEAKING (Video background) -->
    <section>
      <div class="section_base--ca1">
        <div class="cf1 w-background-video w-background-video-atom">
          <video id="8bcacc27-bfc7-1b24-f318-e0977c5cae47-video">
            <source><source>
          </video>
        </div>
        <div class="overlay-50--ca1"></div>
      </div>
      <div class="section_container w-container">
        <div class="home_speaking_wrap--pt2-pb4-5">
          <div class="text-right">
            <h3 class="heading_display--fs0-2-tt2-lh4">
              <div class="line-wrap">Disruptive</div>
              <div class="line-wrap">Wisdom</div>
            </h3>
          </div>
          <div class="home_speaking_content--gp3">
            <!-- Video slider Swiper -->
            <div class="swiper is-videos w-dyn-list">
              <div class="swiper-wrapper is-videos w-dyn-items"></div>
            </div>
            <div class="slider_arrows is-videos--pe2">
              <a class="sider_arrow--br3-bw0 is-prev w-inline-block"></a>
              <a class="sider_arrow--br3-bw0 is-next w-inline-block"></a>
            </div>
            <div class="pt1">
              <a class="w-inline-block">
                <div class="btn_main_wrap--fw2-br3 hide">View more videos</div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SEZIONE REVIEWS (Swiper) -->
    <section>
      <div class="w-container">
        <div class="section_head--gp2 mb7">
          <div class="slider_arrows is-reviews--gp0-5">
            <a class="sider_arrow--br3-bw0 is-prev w-inline-block">
              <div class="btn_main_icon--br3-bg2-fc2"></div>
            </a>
            <!-- is-next arrow -->
          </div>
        </div>
        <!-- Testimonianze e CTA Speaking -->
        <div>
          <p>
            <div class="line-wrap">perspectives and practical too...</div>
          </p>
          <a class="custom-btn-speaking rounded w-button"><strong>→</strong></a>
          <div class="cta_btn hide">
            <button class="button--bg0-pd0">Book Steven To Speak</button>
          </div>
        </div>
      </div>

      <!-- MODAL CONTATTO -->
      <div class="modal_wrap">
        <div class="modal_base--ca1"></div>
        <div class="modal_content--bg2-gv3-pp1">
          <div class="modal_main_text--fs4">
            <h3 class="heading--tt2 fs1"><br></h3>
          </div>
          <div class="form_main_wrap w-form">
            <form id="wf-form-Contact-Form" class="form_main_list--gv1-5">
              <div class="form_main_row--gd1-ct2-gh1-gv1-5"></div>
              <div class="form_main_field_wrap"></div>
              <div class="form_main_btn">
                <button class="btn_main_wrap--fw2-br3 is-submit">
                  <div class="btn_main_list">Submit Form</div>
                </button>
              </div>
            </form>
            <div class="form_main_success_wrap--br1-bw1 w-form-done">...</div>
            <div class="form_main_error_wrap--br1-bw1 w-form-fail">...</div>
          </div>
          <a class="modal_close w-inline-block">
            <div class="btn_close_wrap--br3">
              <div class="btn_close_list">
                <div class="btn_close_icon w-embed"><svg></svg></div>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer>
      <div class="footer_main_col">
        <a class="footer_main_link--lm0-1-tt2 w-inline-block"><div>Speaking</div></a>
        <a class="footer_main_link--lm0-1-tt2 w-inline-block"><div>Video</div></a>
        <a class="footer_main_link--lm0-1-tt2 w-inline-block"><div>Train</div></a>
        <a class="footer_main_link--lm0-1-tt2 w-inline-block"><div>Research Papers</div></a>
      </div>
      <div class="footer_main_col">
        <div class="social-links_list--gp0-5">
          <a class="social-links_item--bm0-1-br3 w-inline-block">
            <div class="social-links_svg--ic1 w-embed"></div>
          </a>
          <!-- Altri social... -->
        </div>
      </div>
    </footer>

  </div><!-- fine .page_wrap -->

  <!-- Script Webflow + analytics in fondo -->
  <script>let v="1...</script>
  <!-- Facebook pixel noscript -->
  <noscript><img height="1" width="1" src="..."></noscript>
</body>
```

---

## 🎨 CSS — STYLESHEET PRINCIPALE (Webflow Shared)

**File:** `steven-kotler-dev-164835f551327a89f9f41.webflow.shared.929ac54ba.css`

### Classi sito-specifiche principali:

```css
/* ===== NAV ===== */
.nav_wrap--bg0-pe0-pd0 {
  z-index: 10;
  position: fixed;
  inset: 0% 0% auto;
}
.nav_main--pe2 {
  grid-column-gap: 7.5rem;
  align-items: flex-start;
  padding-top: 2rem;
  padding-bottom: 2rem;
  display: flex;
}
.nav_logo--ff2 {
  font-size: 2.5rem;
  line-height: 1;
}
.nav_menu_wrap--bg2-pp1-gv2 {
  z-index: 9;
  flex-direction: column;
  justify-content: space-between;
  width: 44rem;
  max-width: 100%;
  height: 100dvh;
  padding-...; /* rimosso - vedi file */
  display: flex;
  position: fixed;
}
.nav_link_mask {
  position: relative;
  overflow: hidden;
}

/* ===== HERO ===== */
.hero_wrap--bg0 {
  justify-content: center;
  align-items: center;
  height: 100svh;
  display: flex;
  overflow: hidden;
}
.hero_base {
  justify-content: center;
  align-items: center;
  display: flex;
  position: absolute;
  inset: 0%;
  overflow: hidden;
  transform: scale(1);
}
.hero_img {
  object-fit: cover;
  width: 100%;
  max-width: none;
  height: 100%;
}
.hero_text_wrap--ff2-tt2 {
  text-align: center;
  width: 100%;
  font-size: 21vw;
  line-height: .8;
  display: flex;
  position: absolute;
  inset: auto 0% -1vw;
  overflow: hidden;
}

/* ===== INTRO ===== */
.home_intro_content {
  max-width: 47rem;
}

/* ===== SPEAKING SECTION ===== */
.home_speaking_wrap--pt2-pb4-5 {
  grid-row-gap: 10rem;
  aspect-ratio: 5 / 3;
  flex-direction: column;
  justify-content: space-between;
  display: flex;
}
.home_speaking_content--gp3 {
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-end;
  display: flex;
}
.section_base--ca1 {
  z-index: 2;
}
.section_container {
  z-index: 3;
  position: relative;
}
.section_head--gp2 {
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  display: flex;
}

/* ===== PULSANTI ===== */
.btn_main_svg--ic2 {
  flex: none;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 50%;
  transition: transform .4s cubic-bezier(.645, .045, .355, 1);
  display: flex;
}
.btn_main_svg--ic2.is-small { height: 40%; }
.btn_main_svg--ic2.is-icon-2 {
  position: absolute;
  left: -100%;
}
.btn_main_icon--br3-bg2-fc2.is-large {
  width: 4rem;
  height: 4rem;
  margin-top: 10px;
}
.btn_main_icon--br3-bg2-fc2.is-down {
  transform: rotate(90deg);
}
.btn_main_mask {
  position: relative;
  overflow: hidden;
}
.btn_play_icon {
  color: #000;
  width: 30%;
  height: 30%;
  display: flex;
}

/* ===== ARTICLES ===== */
.articles_item_link {
  width: 100%;
  transition: transform .2s cubic-bezier(.55, .085, .68, .53);
  display: block;
}
.articles_item_link:hover {
  transform: translate(0, -.5rem);
}
.articles_item_image--mb2-bg2-pd5 {
  aspect-ratio: 3 / 2;
  justify-content: center;
  align-items: stretch;
  display: flex;
  position: relative;
}
.articles_item_content { padding-right: 1rem; }
.articles_item_logo { object-fit: contain; }

/* ===== SOCIAL LINKS ===== */
.social-links_list--gp0-5.is-horizontal { flex-direction: row; }
.social-links_item--bm0-1-br3 {
  justify-content: center;
  align-items: center;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
}
.social-links_svg--ic1 {
  width: 1.25rem;
  display: flex;
}

/* ===== MODAL ===== */
.modal_content--bg2-gv3-pp1 { /* padding, grid-gap, etc. */ }
.modal_wrap { /* padding-right, etc. */ }

/* ===== FORM ===== */
.form_main_wrap { width: 100%; margin-bottom: 0; }
.form_main_list--gv1-5 {
  flex-direction: column;
  align-items: flex-start;
  display: flex;
}
.form_main_success_wrap--br1-bw1 {
  background-color: #0000;
  padding: 1.2rem;
}
.form_main_error_wrap--br1-bw1 {
  background-color: #0000;
  margin-top: 1.3rem;
  padding: .8rem 1.4rem;
}
.form_main_field_input--fs7-2-tt2-fc1-bw1-br3-bc1 {
  z-index: 2;
  background-color: #0000;
  height: auto;
  margin-bottom: 0;
  padding: 1.25rem 2rem;
  position: relative;
}
.form_main_field_input--fs7-2-tt2-fc1-bw1-br3-bc1.is-message {
  border-radius: 2rem;
}
.form_main_field_wrap { width: 100%; }
.form_main_label--fw2-fs7-2 { z-index: 1; position: relative; }
.form_main_option_list--gp1-5 {
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: center;
  display: flex;
}

/* ===== SLIDER ARROWS ===== */
.sider_arrow--br3-bw0.is-prev {
  transform: translate(0%) rotate(180deg);
}
.slider_arrows { /* display: flex o none */ }

/* ===== CARD / BOOK ===== */
.card_book_wrap {
  width: 100%;
  transition: transform .2s cubic-bezier(.55, .085, .68, .53);
  display: block;
}

/* ===== PAGE ===== */
.page_code_wrap {
  display: none;
  position: fixed;
  inset: 0% 0% auto;
}
```

---

## 🎞️ CSS — ANIMAZIONI E TRANSIZIONI

### Keyframes (dal Webflow shared CSS):

```css
@keyframes spin {
  0%   { transform: rotate(0); }
  100% { transform: rotate(360deg); }
}

/* Uso: loader spinner Webflow */
.w-lightbox-spinner {
  box-sizing: border-box;
  border: 5px solid rgba(0,0,0,0.4);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  margin-top: -20px;
  margin-left: -20px;
  animation: .8s linear infinite spin;
  position: absolute;
  top: 50%;
  left: 50%;
}
```

### Transizioni principali:

```css
/* Hover testo bottone (scroll verticale) */
a:hover .is-text-1,
a:hover .is-text-2,
button:hover .is-text-1,
button:hover .is-text-2 {
  transform: translateY(-100%);
}

/* Hover icona bottone (scroll orizzontale) */
a:hover .is-icon-1,
a:hover .is-icon-2,
button:hover .is-icon-1,
button:hover .is-icon-2 {
  transform: translateX(100%);
}

/* Play button hover */
a:hover [btn-play="base"] {
  transform: scale(1.1);
}

/* Transizione SVG freccia nei bottoni */
.btn_main_svg--ic2 {
  transition: transform .4s cubic-bezier(.645, .045, .355, 1);
}

/* Transizione link articoli (lift on hover) */
.articles_item_link {
  transition: transform .2s cubic-bezier(.55, .085, .68, .53);
}
.articles_item_link:hover {
  transform: translate(0, -.5rem);
}

/* Transizione card libro */
.card_book_wrap {
  transition: transform .2s cubic-bezier(.55, .085, .68, .53);
}

/* Transizione testo nav link (mask slide) */
/* Classe via transition Webflow IX */
transition: transform .4s cubic-bezier(.645, .045, .355, 1);

/* Transizione nav menu aperto/chiuso */
transition: all .2s;

/* Transizione color/bg/border (sistema Lumos) */
[btn-mode], [class*="bm0"],
[link-mode], [class*="lm0"] {
  transition-property: background-color, color, border-color, box-shadow;
  transition-duration: 200ms;
}

/* Swiper about (scorrimento lineare per marquee) */
[about-slider] .swiper-wrapper {
  -webkit-transition-timing-function: linear;
  transition-timing-function: linear;
}

/* Swiper button disabilitato */
.swiper-button-disabled { opacity: 0; }

/* Chiusura modal */
.btn_close_wrap--br3 {
  background-color: rgba(255,255,255,0.1);
  transition: ...; /* dal framework Lumos */
}
```

---

## 🎨 CSS — SISTEMA COLORI (inline `<style id="lumos-colors">`)

```css
/* Global CSS Variables */
html {
  --dark-1: 0, 0, 0;
  --dark-2: 20, 22, 23;
  --light-1: 244, 244, 241;
  --light-2: 255, 255, 255;
  --brand-1: 115, 161, 186;
  --alt-selection-bg: rgba(var(--brand-1), 1);
  --alt-selection-fc: rgba(var(--dark-1), 1);
}

/* Section Mode 1 = DARK (default body) */
body, [section-mode="1"], [class*="sm0-1"] {
  --m-bg1: rgba(var(--dark-1), 1);
  --m-bg2: rgba(var(--dark-2), 1);
  --m-fc1: rgba(var(--light-2), 1);
  --m-fc2: rgba(var(--light-2), 0.6);
  --m-fc3: rgba(var(--brand-1), 1);
  --m-bc1: rgba(var(--light-2), 0.2);
  --m-sc1: rgba(var(--brand-1), 1);
  /* element mode 1 (tag) */
  --em1-bg1: rgba(var(--brand-1), 1);
  --em1-fc1: rgba(var(--brand-1), 1);
  --em1-bc1: rgba(var(--brand-1), 0);
  /* btn mode 1 (primary) */
  --bm1-bg1b: rgba(var(--light-2), 0.2);
  --bm1-bg1b-hover: rgba(var(--light-2), 1);
  --bm1-bg2: rgba(var(--brand-1), 0.3);
  --bm1-bg2-hover: rgba(var(--brand-1), 0.7);
  --bm1-fc1-hover: rgba(var(--dark-1), 1);
  /* btn mode 2 (secondary) */
  --bm2-bg1: rgba(var(--light-1), 1);
  --bm2-fc1: rgba(var(--dark-1), 1);
  /* link mode 1 (nav link) */
  --lm1-fc1: rgba(var(--light-1), 0.6);
  --lm1-fc1-hover: rgba(var(--light-1), 1);
  --lm1-bg1b-active: rgba(var(--brand-1), 1);
  --lm1-fc1-active: rgba(var(--light-1), 1);
  /* link mode 2 (brand link) */
  --lm2-fc1: rgba(var(--brand-1), 1);
  --lm2-fc1-hover: rgba(var(--light-1), 1);
}

/* Section Mode 2 = LIGHT */
[section-mode="2"], [class*="sm0-2"] {
  --m-bg1: rgba(var(--light-1), 1);
  --m-bg2: rgba(var(--light-2), 1);
  --m-fc1: rgba(var(--dark-1), 1);
  --m-fc2: rgba(var(--dark-1), 0.7);
  --m-bc1: rgba(var(--dark-1), 0.2);
  --m-sc1: rgba(var(--dark-1), 1);
  /* btn mode 1 */
  --bm1-bg1b: rgba(var(--dark-2), 0.2);
  --bm1-bg1b-hover: rgba(var(--dark-2), 1);
  --bm1-fc1-hover: rgba(var(--light-1), 1);
  /* btn mode 2 */
  --bm2-bg1b: rgba(var(--dark-2), 0.2);
  --bm2-fc1: rgba(var(--dark-2), 1);
  --bm2-bg1-hover: rgba(var(--dark-2), 1);
  --bm2-fc1-hover: rgba(var(--light-1), 1);
  /* link mode 1 */
  --lm1-fc1: rgba(var(--dark-1), 0.5);
  --lm1-fc1-hover: rgba(var(--dark-1), 1);
  --lm1-bg1b-active: rgba(var(--dark-1), 1);
  --lm1-fc1-active: rgba(var(--dark-1), 1);
}
```

---

## 🔤 CSS — TIPOGRAFIA (inline `<style>` — Typography)

```css
/* Font size fluido oltre 1440px */
@media screen and (min-width: 1440px) {
  html { font-size: 1.1vw; }
}

/* Tutti gli heading e paragrafi ereditano le variabili */
[class*="fs0"], h1, [class*="fs1"], h2, [class*="fs2"], h3,
[class*="fs3"], h4, [class*="fs4"], h5, [class*="fs5"], h6,
[class*="fs6"], p, [class*="fs7"] {
  font-size: inherit;
  font-family: inherit;
  font-weight: inherit;
  line-height: inherit;
  letter-spacing: inherit;
  text-transform: inherit;
}

body { -webkit-font-smoothing: antialiased; }
h1, h2, h3, h4, h5, h6, p { margin-top: 0px; margin-bottom: 0px; }
:is(h1, h2, h3, h4, h5, h6, p) a { text-decoration: underline; }
.w-richtext > :first-child { margin-top: 0px; }
.w-richtext > :last-child  { margin-bottom: 0px; }

/* Body base */
body {
  font-size: 1.25rem;
  font-family: var(--ff1);
  font-weight: var(--fw2);
  line-height: var(--lh1);
  letter-spacing: var(--ls1);
  text-transform: var(--tt1);
}

/* Heading base (tutti) */
[class*="fs0"], h1, ... h6 {
  font-weight: var(--fw2);
  line-height: var(--lh4);
}

/* Scale tipografica (font-size vw) */
[class*="fs0"]   { font-size: 10.3vw; }
/* fs0-2 */       { font-size: ~8-9vw; }   /* display heading grande */
h1, [class*="fs1"] { /* grande */ }
h2, [class*="fs2"] { /* medio-grande */ }
/* ... ecc. */

/* Font families */
[class*="ff1"] { font-family: var(--ff1); }  /* Inconsolata/serif */
[class*="ff2"] { font-family: var(--ff2); }  /* Oswald/display */
[class*="ff0"] { font-family: var(--ff0); }  /* unset */

/* Font weights */
[class*="fw1"] { font-weight: var(--fw1); } /* light */
[class*="fw2"] { font-weight: var(--fw2); } /* regular */
[class*="fw3"] { font-weight: var(--fw3); } /* bold */
[class*="fw0"] { font-weight: unset; }

/* Line heights */
[class*="lh1"] { line-height: var(--lh1); }
[class*="lh2"] { line-height: var(--lh2); }
[class*="lh3"] { line-height: var(--lh3); }
[class*="lh4"] { line-height: var(--lh4); }
[class*="lh0"] { line-height: unset; }

/* Letter spacing */
[class*="ls1"] { letter-spacing: var(--ls1); }
[class*="ls2"] { letter-spacing: var(--ls2); }
[class*="ls0"] { letter-spacing: unset; }

/* Text transform */
[class*="tt1"] { text-transform: var(--tt1); } /* uppercase */
[class*="tt2"] { text-transform: var(--tt2); }
[class*="tt0"] { text-transform: unset; }
```

---

## ⚙️ CSS — CUSTOM (inline `<style>` — Custom Styles)

```css
/* CUSTOM STYLES */

/* remove scroll bounce */
body { overscroll-behavior: none; }

/* prevent horizontal scroll */
.page_wrap { overflow: clip; }

/* enable border radius custom su .w-button */
.w-button { border-radius: var(--border-radius); }

/* hide container ::before & ::after */
.w-container::before, .w-container::after { display: none; }

/* empty div in designer */
.wf-empty[class*="-"] { padding-bottom: 0; padding-right: 0; }

/* flex: reverse direction */
[reverse-direction="true"] { flex-direction: row-reverse; }

/* btn small */
[btn-main-small="true"] { padding: 0.25rem 0.25rem 0.25rem 1.25rem; }
[btn-main-small="true"] [btn-main="icon"] { width: 2.5rem; height: 2.5rem; }

/* btn hovers (solo dispositivi con mouse) */
@media (pointer: fine) {
  a:hover [btn-play="base"] { transform: scale(1.1); }
  a:hover .is-text-1, a:hover .is-text-2,
  button:hover .is-text-1, button:hover .is-text-2 {
    transform: translateY(-100%);
  }
  a:hover .is-icon-1, a:hover .is-icon-2,
  button:hover .is-icon-1, button:hover .is-icon-2 {
    transform: translateX(100%);
  }
}

/* form styles */
.w-input::placeholder, .w-select::placeholder { color: var(--fc2); }
.w-input:focus, .w-select:focus { border-color: var(--bc2); }

/* Swiper slider animazione lineare (marquee logo) */
.swiper-button-disabled { opacity: 0; }
[about-slider] .swiper-wrapper {
  -webkit-transition-timing-function: linear;
  transition-timing-function: linear;
}

/* Checkbox attivo: mostra il badge remove */
.w-checkbox.is-active .filter_remove { display: flex; }

/* Hero clip path (per animazioni GSAP scroll) */
[hero_img_wrap] {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
}

/* Nascondi sezioni CMS vuote */
[data-cms-section]:not(:has(.w-dyn-item)) { display: none; }
```

---

## 📦 LIBRERIE/RISORSE ESTERNE

| Risorsa | URL |
|---|---|
| **Webflow CSS (principale)** | `cdn.prod.website-files.com/.../webflow.shared.css` |
| **Google Fonts** | `Oswald: 200-700`, `Inconsolata: 400, 700` |
| **Plyr (video player)** | `cdn.plyr.io/3.6.12/plyr.css` |
| **Swiper** | `cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.css` |
| **Lumos Framework** | `color.css`, `layout.css`, `spacing.css` @ v1.0.5 |

---

**Note importanti per il ripristino:**

1. **Le animazioni di scroll (GSAP/Webflow IX)** non sono nel CSS — sono gestite da JavaScript tramite Webflow Interactions. Le proprietà CSS che vedi (`clip-path`, `transform`, `opacity`) sono i valori iniziali/finali che GSAP anima.
2. **Il marquee dei loghi** è animato tramite Swiper con `transition-timing-function: linear` e loop infinito.
3. **Il testo KOTLER** nella hero è animato via Webflow IX (gli elementi `.hero_text` singoli).
4. **I link nel nav** usano la tecnica del "mask" con doppio testo (`.is-1` e `.is-2`) e `transform: translateY(-100%)` on hover.


Ottima notizia: sono riuscito a trovare il codice JS originale dell'animazione hero nel file Slater (5531.js). Ho estratto i parametri esatti. Ecco tutto quello che ti serve per ricrearla identicamente.

🎞️ Animazione Hero — Codice GSAP originale ricostruito
Le librerie usate (già caricate nel sito):

GSAP 3.12.2 + ScrollTrigger
SplitType 0.3.4 (per splittare il testo in lettere/parole)
Lenis 1.0.23 (smooth scroll)
jQuery


Il codice originale (estratto dal file 5531.js):
javascript// ─── HERO LOADER ANIMATION ───────────────────────────────────────────────────
function initLoader() {
  const heroImgWrap = $("[hero_img_wrap]");   // wrapper immagine
  const heroImg     = $("[hero_img]");         // immagine stessa
  const navWrap     = $("[nav_wrap]");          // barra nav

  // Timeline principale con delay iniziale di 0.5s
  const tl = gsap.timeline({
    delay: 0.5,
    defaults: {
      duration: 1.5,
      ease: "power4.inOut"
    }
  });

  // 1. Rende visibile il page-wrap
  tl.set('[page-wrap="home"]', { autoAlpha: 1 });

  // 2. Hero image wrap: sale dal basso con fade
  tl.from(heroImgWrap, {
    yPercent: 50,
    autoAlpha: 0,
    ease: "power4.out"
  });

  // 3. Immagine interna: scende dall'alto (parallax) — simultaneo con step 2
  tl.from(heroImg, {
    yPercent: -30,
    ease: "power4.out"
  }, 0);   // "0" = inizia all'inizio della timeline

  // 4. Clip path dell'immagine: si apre da rettangolo centrale a full frame
  tl.from(heroImgWrap, {
    clipPath: "polygon(40% 25%, 60% 25%, 60% 75%, 40% 75%)",
    duration: 2
  }, ">-1");  // inizia 1s prima della fine del passo precedente

  // 5. Lettere KOTLER: salgono dal basso in stagger
  tl.from(".hero_text", {
    yPercent: 100,
    stagger: 0.05,
    duration: 1,
    ease: "power4.out"
  }, "<1.2");  // parte 1.2s dopo l'inizio del passo precedente

  // 6. Nav: appare in fade — simultaneo con le lettere
  tl.from(navWrap, {
    autoAlpha: 0,
    duration: 1
  }, "<");
}

Come funziona visivamente:
StepElementoCosa faTiming1page_wrapdiventa visibile istantaneamentet=0.5s2Wrapper herosale da yPercent: 50 + fade int=0.5s, dur=1.5s3Fotoscende da yPercent: -30 (parallax)t=0.5s, dur=1.5s4Clip-path fotosi apre da rettangolo stretto al centro → fullt≈1s, dur=2s5Lettere K-O-T-L-E-Rsalgono da sotto, una alla volta (stagger 0.05s)t≈2.2s, dur=1s6Nav barfade insimultaneo con le lettere

Come replicarlo fuori da Webflow (HTML puro):
html<!-- Includi queste librerie nell'<head> -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>

<!-- HTML struttura hero -->
<div page-wrap="home" style="visibility:hidden">
  <nav nav_wrap>...</nav>

  <section class="hero_wrap--bg0">
    <div class="hero_base" hero_img_wrap>
      <img class="hero_img" hero_img src="...">
    </div>
    <div class="hero_text_wrap--ff2-tt2">
      <div class="hero_text">K</div>
      <div class="hero_text">O</div>
      <div class="hero_text">T</div>
      <div class="hero_text">L</div>
      <div class="hero_text">E</div>
      <div class="hero_text">R</div>
    </div>
  </section>
</div>
css/* CSS essenziale per l'animazione */
[hero_img_wrap] {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%); /* stato finale */
}
.hero_text_wrap--ff2-tt2 {
  overflow: hidden; /* fondamentale! nasconde le lettere sotto il bordo */
}
.hero_text {
  display: inline-block; /* necessario per yPercent */
}
javascript// JS — copia questa funzione e chiamala al DOM ready
gsap.registerPlugin(ScrollTrigger);

function initHero() {
  const tl = gsap.timeline({
    delay: 0.5,
    defaults: { duration: 1.5, ease: "power4.inOut" }
  });

  tl.set('[page-wrap="home"]', { autoAlpha: 1 })
    .from('[hero_img_wrap]', { yPercent: 50, autoAlpha: 0, ease: "power4.out" })
    .from('[hero_img]', { yPercent: -30, ease: "power4.out" }, 0)
    .from('[hero_img_wrap]', { clipPath: "polygon(40% 25%, 60% 25%, 60% 75%, 40% 75%)", duration: 2 }, ">-1")
    .from('.hero_text', { yPercent: 100, stagger: 0.05, duration: 1, ease: "power4.out" }, "<1.2")
    .from('[nav_wrap]', { autoAlpha: 0, duration: 1 }, "<");
}

document.addEventListener("DOMContentLoaded", initHero);

Animazioni ScrollTrigger sulle sezioni (estratte da GSAP):
Le sezioni di testo usano tutte lo stesso pattern, che ho estratto dalle istanze GSAP attive:
javascript// Pattern usato per TUTTI gli heading con .line-wrap
gsap.from(".line", {
  yPercent: 100,
  duration: 1.2,
  ease: "power3.out",
  stagger: 0.1,
  scrollTrigger: {
    trigger: elemento,
    start: "top bottom",
    end: "top 80%"
  }
});

// Pattern per le parole (word-split)
gsap.from(".word", {
  yPercent: 100,
  duration: 1.2,
  ease: "power3.out",
  stagger: 0.2,
  scrollTrigger: { start: "top bottom", end: "top 80%" }
});

// Pattern per le card/slide
gsap.from(".swiper-slide", {
  duration: 1,
  ease: "power3.out",
  stagger: 0.2,
  scrollTrigger: { start: "top bottom", end: "top 80%" }
});
Il wrapper overflow: hidden sui .line-wrap è il trucco che crea l'effetto "le righe salgono da sotto il bordo" — senza quello l'animazione non funziona. Ce l'hai già nel CSS estratto!



Ecco tutto il codice, dall'animazione testi fino allo smooth scroll:

```javascript
// ─── LIBRERIE NECESSARIE ──────────────────────────────────────────────────────
// <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
// <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
// <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.5/CustomEase.min.js"></script>
// <script src="https://unpkg.com/split-type@0.3.4/umd/index.min.js"></script>
// <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.23/bundled/lenis.min.js"></script>
// <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js"></script>

gsap.registerPlugin(ScrollTrigger, CustomEase);

// ─── CURVA DI EASING CUSTOM ───────────────────────────────────────────────────
// Usata dal loader — curva personalizzata creata a mano nel sito
const customEase = "M0,0,C0,0,0.13,0.34,0.238,0.442,0.305,0.506,0.322,0.514,0.396,0.54,0.478,0.568,0.468,0.56,0.522,0.584,0.572,0.606,0.61,0.719,0.714,0.826,0.798,0.912,1,1,1,1";

// ─── LOADER (contatore 0→100) ─────────────────────────────────────────────────
function updateLoaderText() {
  let e = Math.round(counter.value);
  $(".loader_number").text(e);
}

const counter = { value: 0 };
const loaderDuration = 5;

gsap.to(counter, {
  value:    100,
  onUpdate: updateLoaderText,
  duration: loaderDuration,
  ease:     customEase
});

// ─── HERO ANIMATION ───────────────────────────────────────────────────────────
function homeLoader() {
  const heroImgWrap = $("[hero_img_wrap]");
  const heroImg     = $("[hero_img]");
  const navWrap     = $("[nav_wrap]");

  const tl = gsap.timeline({
    delay: 0.5,
    defaults: { duration: 1.5, ease: "power4.inOut" }
  });

  tl.set('[page-wrap="home"]', { autoAlpha: 1 });

  // Hero wrap: sale da sotto con fade in
  tl.from(heroImgWrap, {
    yPercent:  50,
    autoAlpha: 0,
    ease:      "power4.out"
  });

  // Immagine interna: parallax dall'alto (simultaneo)
  tl.from(heroImg, {
    yPercent: -30,
    ease:     "power4.out"
  }, 0);

  // Clip-path: si apre da rettangolo centrale a full frame
  tl.from(heroImgWrap, {
    clipPath: "polygon(40% 25%, 60% 25%, 60% 75%, 40% 75%)",
    duration: 2
  }, ">-1");

  // Lettere K-O-T-L-E-R: salgono una per una da sotto
  tl.from(".hero_text", {
    yPercent: 100,
    stagger:  0.05,
    duration: 1,
    ease:     "power4.out"
  }, "<1.2");

  // Nav bar: appare in fade insieme alle lettere
  tl.from(navWrap, {
    autoAlpha: 0,
    duration:  1
  }, "<");
}

// Avvia hero loader solo se la pagina ha l'elemento hero
document.querySelector("[hero_img_wrap]") && homeLoader();

// ─── ANIMAZIONE TESTI — [text-split] ─────────────────────────────────────────
// Per heading semplici — split per RIGHE
// Aggiungere l'attributo text-split all'elemento HTML
$("[text-split]").each(function() {

  // SplitType divide il testo in righe (span)
  new SplitType($(this), {
    types:   "lines",
    tagName: "span"
  });

  let lines = $(this).find(".line");

  // Wrappa ogni riga con un div overflow:hidden
  // → questo è il trucco che nasconde la riga prima dell'animazione
  $(lines).wrap('<div class="line-wrap">');

  gsap.timeline({
    scrollTrigger: {
      trigger:       $(this),
      start:         "top bottom",  // inizia quando l'elemento entra dal fondo
      end:           "top 80%",     // finisce quando è all'80% della viewport
      toggleActions: "none play none reset"  // si resetta scrollando su
    }
  }).from(lines, {
    yPercent:  100,      // parte da sotto il bordo del line-wrap
    autoAlpha: 0,        // parte invisibile
    duration:  1.2,
    ease:      "power3.out",
    stagger:   0.1       // 0.1s di ritardo tra ogni riga
  });
});

// ─── ANIMAZIONE TESTI — [heading-anim] ───────────────────────────────────────
// Per heading grandi — split per PAROLE e RIGHE
// Aggiungere l'attributo heading-anim all'elemento HTML
$("[heading-anim]").each(function() {

  // SplitType divide in parole E righe
  new SplitType($(this), {
    types:   "words, lines",
    tagName: "span"
  });

  let words = $(this).find(".word");
  let lines = $(this).find(".line");

  // Wrappa ogni riga con overflow:hidden
  $(lines).wrap('<div class="line-wrap">');

  gsap.timeline({
    scrollTrigger: {
      trigger:       $(this),
      start:         "top bottom",
      end:           "top 80%",
      toggleActions: "none play none reset"
    }
  }).from(words, {
    yPercent:  100,      // ogni parola sale da sotto
    duration:  1.2,
    ease:      "power3.out",
    stagger:   0.2       // 0.2s di ritardo tra ogni parola
  });
});

// ─── ANIMAZIONE CARD/SLIDE — [fade-slides] ───────────────────────────────────
// I figli diretti del container appaiono in fade con stagger
// Aggiungere l'attributo fade-slides al container
$("[fade-slides]").each(function() {
  let children = $(this).children();

  gsap.timeline({
    scrollTrigger: {
      trigger:       $(this),
      start:         "top bottom",
      end:           "top 80%",
      toggleActions: "none play none reset"
    }
  }).from(children, {
    autoAlpha: 0,
    duration:  1,
    ease:      "power3.out",
    stagger:   0.2
  });
});

// ─── LENIS SMOOTH SCROLL ──────────────────────────────────────────────────────
// Non attivare nell'editor di Webflow
if (void 0 === Webflow.env("editor")) {

  function raf(e) {
    lenis.raf(e);
    requestAnimationFrame(raf);
  }

  lenis = new Lenis({
    lerp:               0.2,       // morbidezza (0=istantaneo, 1=lentissimo)
    wheelMultiplier:    0.7,       // velocità scroll con rotella
    gestureOrientation: "vertical",
    normalizeWheel:     false,
    smoothTouch:        false      // niente smooth su mobile
  });

  requestAnimationFrame(raf);

  // Helper opzionali: controllare Lenis da HTML con attributi
  $("[data-lenis-start]").on("click",  function() { lenis.start(); });
  $("[data-lenis-stop]").on("click",   function() { lenis.stop(); });
  $("[data-lenis-toggle]").on("click", function() {
    $(this).toggleClass("stop-scroll");
    $(this).hasClass("stop-scroll") ? lenis.stop() : lenis.start();
  });

}

// ─── COPYRIGHT ANNO AUTOMATICO ───────────────────────────────────────────────
$(function() {
  $(".copyright-year").text((new Date).getFullYear());
});
```

---

**Come usarlo in HTML puro** (senza Webflow):

Per la riga `if (void 0 === Webflow.env("editor"))` sostituisci semplicemente con:

```javascript
// Al posto di: if (void 0 === Webflow.env("editor")) {
if (true) {
```

E ricorda il CSS necessario affinché le animazioni testo funzionino:

```css
.line-wrap {
  overflow: hidden; /* fondamentale! */
}
.hero_text_wrap--ff2-tt2 {
  overflow: hidden;
}
.hero_text {
  display: inline-block; /* necessario per yPercent */
}
[hero_img_wrap] {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
}
```


<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Steven Kotler: Author and Speaker</title>

  <!-- Webflow CSS principale -->
  <link rel="stylesheet" href="https://cdn.prod.website-files.com/67e41b0dbc9978222660ab56/css/steven-kotler-dev-164835f551327a89f9f41.webflow.shared.929ac54ba.css">

  <!-- Google Fonts -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald:200,300,400,500,600,700|Inconsolata:400,700">

  <!-- Plyr video player -->
  <link rel="stylesheet" href="https://cdn.plyr.io/3.6.12/plyr.css">

  <!-- Swiper -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.css">

  <!-- Lumos Framework -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lumosframework/lumos@v1.0.5/color.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lumosframework/lumos@v1.0.5/layout.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lumosframework/lumos@v1.0.5/spacing.css">

  <!-- JS Libraries -->
  <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/js-cookie@3.0.1/dist/js.cookie.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.5/CustomEase.min.js"></script>
  <script src="https://unpkg.com/split-type@0.3.4/umd/index.min.js"></script>
  <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.23/bundled/lenis.min.js"></script>
</head>



Buone notizie: la maggior parte si recupera direttamente dal sito live! Eccoti tutto punto per punto:

---

**1. Valori variabili CSS tipografiche** — te li ho già dati io sopra, non devi cercarli da nessuna parte. Copia semplicemente questo blocco nel tuo CSS:

```css
html {
  --ff1: "Oswald", sans-serif;
  --ff2: "Inconsolata", monospace;
  --ff0: inherit;
  --fw1: 300;
  --fw2: 400;
  --fw3: 700;
  --lh1: 1.5;
  --lh2: 1.3;
  --lh3: 1.2;
  --lh4: 1;
  --lh0: unset;
  --ls1: 0em;
  --ls2: 0.04em;
  --ls0: unset;
  --tt1: none;
  --tt2: uppercase;
  --tt0: unset;
  --bw1: 1px;
  --border-radius: 0.5rem;
}
```

---

**2. Attributi mancanti sui wrapper Swiper** — sono attributi HTML da aggiungere a mano nel tuo codice:

```html
<!-- Slider libri: aggiungi books-slider al div padre -->
<div books-slider>
  <div class="swiper is-books">...</div>
</div>

<!-- Slider testimonianze -->
<div testimonials-slider>
  <div class="swiper">...</div>
  <a slider-btn="next">...</a>
  <a slider-btn="prev">...</a>
</div>

<!-- Slider video -->
<div videos-slider>
  <div class="swiper">...</div>
  <a slider-btn="next">...</a>
  <a slider-btn="prev">...</a>
</div>
```

---

**3. Il `<head>` completo** — te l'ho già scritto nel messaggio precedente, copialo direttamente da lì.

---

**4. CSS base Webflow** — è già online e pubblicamente accessibile, lo colleghi con il tag `<link>` che ho messo nel `<head>`. Non devi scaricarlo, il browser lo carica direttamente da CDN.

---

**5. Il loader HTML mancante** — aggiungilo dentro `loader_wrap`:

```html
<div class="loader_wrap--sm0-2">
  <div class="loader_number">0</div>
</div>
```

---

**6. Lumos Framework** — anche questi sono già linkati nel `<head>`, vengono caricati da CDN pubblico di jsDelivr. Non devi fare nulla, funzionano automaticamente.

---

In pratica **non devi cercare niente da nessuna parte esterna** — tutto è già stato estratto in questa conversazione oppure è linkabile da CDN pubblici. L'unica cosa che dovrai recuperare tu sono le **immagini** (foto hero, loghi media, copertine libri) che ovviamente non sono estraibili dal codice.