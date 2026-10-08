# 06 · Page coverage — which pages, sections, overlays and states a theme must design

A reference site rarely shows every page an ikas store needs (gizem's reference had no cart page, auth, account or 404). This file is the floor: intake pre-ticks the default scope, the plan's §6.3 lists every page in scope, and CHK `pages` / `overlays` compare the canvas against it.

## Contents
1. Global rules
2. Coverage matrix
3. Required overlays
4. States
5. Sections the reference does not have
6. Custom pages

## 1. Global rules

- **Header + Footer on every page.** In ikas they are global (`isHeader` / `isFooter`) and render automatically; on the canvas every `P/Page/<Name>@device` still starts with a Header instance and ends with a Footer instance so the page reads complete.
- Pages contain **only Section instances** (`ref` to `P/Section/<Key>@<same device>`), in order, nothing loose (CHK `pages`).
- Each page exists at both widths: `P/Page/<Name>@desktop` (1440) and `@mobile` (390).
- One section per concern (product detail, reviews and carousels are separate sections); the same Section may appear on several pages (ProductList on Category, Collection, Search, Favorites).
- Page names on the canvas are English PascalCase (`Home`, `Category`, `Product`, `Cart`, `Account`, `Auth`, `NotFound`, `Search`, `Favorites`…); page-type ids are ikas enum names.

## 2. Coverage matrix

✓ = default in scope (pre-ticked in intake) · ○ = optional (asked in intake) · Templates: `04-ikas-constraints.md` §8.

| Page type | ikas template | Required sections (between Header and Footer) | Overlays | States to draw | Default |
|---|---|---|---|---|---|
| `INDEX` | `hero-slider-section`, `product-slider-section`, `category-images-section`, `features-section` or `(özel)` | hero · ≥1 product row (carousel or grid) · category entry · ≥1 brand/editorial block | Cart, Search, Menu | hero slide n of N; product card states via Subs | ✓ |
| `CATEGORY` | `category-list-section` | ProductList (title, filter/sort bar, grid, pagination or load-more) | Cart, Search, Menu, **FilterDrawer@mobile** | empty (no products), loading (skeleton / load-more spinner), filter applied | ✓ |
| `PRODUCT_DETAIL` | `product-detail-section` (+ `variant-selection`, `add-to-cart`, `product-pricing`, `image-handling`), `product-reviews-section` ○, `product-slider-section` | ProductDetail (gallery, name, price, variants, add-to-cart, description) · ≥1 ProductCarousel (related) | Cart (after add), size guide / info drawer if designed | variant selected / unavailable / out of stock · add-to-cart loading / added · discounted price | ✓ |
| `CART` | `cart-section` | CartPage (lines, quantity, remove, coupon, summary, checkout) | — | empty · filled · line updating (loading) · coupon error | ✓ |
| `ACCOUNT` | `account-info-section` | Account (tabs: info, orders, addresses, favorites, order detail) | ConfirmModal (delete address) ○ | each tab · orders empty · form saving / success / error | ✓ |
| `LOGIN` | `login-section` | AuthForms (login variant) | — | default · field error · submitting | ✓ |
| `REGISTER` | `register-section` | AuthForms (register variant) | — | default · field error · submitting | ✓ |
| `FORGOT_PASSWORD` | `forgot-password-section` | AuthForms (forgot variant) | — | default · success (mail sent) · error | ✓ |
| `RECOVER_PASSWORD` | `recover-password-section` | AuthForms (recover variant) | — | default · success · invalid/expired token | ✓ |
| `NOT_FOUND` | `not-found-section` | NotFound (big title, text, link home) | — | — | ✓ |
| `SEARCH` | `category-list-section` (search mode) | ProductList with search heading (query + result count) | Search | results · no results · loading | ✓ |
| `FAVORITES` | `favorites` pattern + ProductList grid | ProductList (favorites heading) | — | empty (logged in) · logged-out prompt · filled | ✓ |
| `BLOG` | `blog-home-section` | blog listing (cards or rows, category tabs, pagination) | — | empty category | ○ |
| `BLOG_POST` | `blog-post-section` | BlogPost (title, date, image, rich text) · related posts | — | — | ○ |
| `COLLECTION` | `category-list-section` or custom page | CollectionHero `(özel)` · ProductList | as CATEGORY | as CATEGORY | ○ |
| `CUSTOMER_EMAIL_VERIFICATION` | `email-verification-section` | EmailVerification | — | verifying (loading) · success · error | ○ |
| Contact (custom page, `CUSTOM`) — **always custom, full-width, never a narrow form** | `(özel)` + ikas contact form API: `getContactForm` / `initContactForm`, `setContactFormFirstName` · `LastName` · `Email` · `Phone` · `Message`, `submitContactForm(form) → Promise<boolean>` (model `IkasContactForm`) | Composed of several sections, not one cramped block: **ContactForm** (oversized heading + intro + response-time note; wide form card with topic chips, first/last name, email, optional phone, optional order number, message, consent, submit, result message; beside it a column of channel cards: e-mail, phone, a dark chat/WhatsApp card, social) · **StoreLocator** (featured store image with info card + selectable store list with open status) · **FaqList** (title column + accordion) | — | default · sending · success · field error + submit error | ✓ |
| custom page | `rich-text-section` or `(özel)` sections | About, Contact, Support/policy, landing pages — whatever the reference shows | — | form: default · sending · success · error | ○ |

Auth pages may share one Section (`AuthForms`) with four variants drawn as separate frames or states; the plan's §6.3 then lists them as `Auth (×4)` (gizem convention). Header and Footer are counted once each in the section total, not per page.

## 2a. ikas ready-made pages (asked in intake)

ikas renders two page groups with its own components when the merchant enables them (`list_ready_made_pages`, `enable_ready_made_pages`, `update_ready_made_page_prop`):

| Group | Page types | If "ikas hazır" | If "özel" |
|---|---|---|---|
| membership | LOGIN, REGISTER, FORGOT_PASSWORD, RECOVER_PASSWORD, CUSTOMER_EMAIL_VERIFICATION | no AuthForms / EmailVerification section and no page frames for these types; plan §6.3 lists them as `ikas hazır`; the handoff tells the port to enable the group and bind logo + palette (theme globals) + labels via `update_ready_made_page_prop` | design AuthForms (4 variants) + EmailVerification as in §2 |
| account | ACCOUNT, orders, order detail, addresses, FAVORITES | no Account section and no Favorites page frame; same port steps | design Account (tabs) + Favorites (ProductList mode) as in §2 |

The answer is recorded per group in `docs/00-brief.md` §5. A ready-made page still follows the theme's palette and logo, so DS colours and the wordmark must be ready before the port binds them.

## 3. Required overlays

Every theme designs these four, each as its own root frame per state (`P/Overlay/<Name>@desktop — <state>` 1440×900, `@mobile — <state>` 390×844), panel on a flat `$color-scrim` background, never on a copy of a page:

| Overlay | Owner section | States (minimum) |
|---|---|---|
| `CartDrawer` (mini cart) | Header | empty · filled · loading |
| `SearchOverlay` | Header | open empty · typing with results · no results |
| `MenuOverlay` / `MobileMenu` | Header | open (desktop may be a mega menu; mobile is required) |
| `FilterDrawer` | ProductList | `@mobile` open (desktop only if filters are a drawer there too) |

Optional, when the reference or brief has them: Megamenu, InfoDrawer / size guide (ProductDetail), QuickView, ConfirmModal, Toast, cookie bar (Header child), newsletter popup. Overlays port as sub-components rendered by the owner section (`04-ikas-constraints.md` §6).

## 4. States

- **Where states live:** interactive component states (hover, disabled, loading, selected, out of stock, error) are drawn once on `P/Sub/<Name> — <state>` frames, never repeated inside sections. Page-level states (empty cart, no results, empty orders) are separate Section frames named `P/Section/<Key>@device — <state>` only when the layout changes; otherwise a Sub state is enough.
- **Empty:** every list that can be empty (cart, search, category, favorites, orders, addresses, blog category) has an empty state with a TEXT title, TEXT body and a LINK action.
- **Loading:** buttons (spinner + `…ingText` prop), product grids (skeleton cards or load-more spinner), cart line updates.
- **Error / success:** every form (auth, newsletter, contact, address, coupon, review) has field error and submit error, and a success message where the flow ends on the same page. Copy for each is a TEXT prop (two props for button loading labels).
- **Commerce states:** discounted price (compare-at struck through), out of stock (badge + disabled add-to-cart + back-in-stock option), variant unavailable, free-shipping progress if designed.

## 5. Sections the reference does not have

When the reference lacks a required page (common: cart, auth, account, 404, search, favorites), design it in the same visual language and record it in `components.md` §1 under "Referansta olmayan ama ikas'ta gereken sayfalar" with its template. Do not mark these values `[ölçüldü]`; their structure comes from the ikas template, their look from the theme tokens.

## 6. Custom pages

Custom pages (About, Contact, Support, campaign landing) are created by the merchant with `create_page`. **Contact is in scope by default** (pre-ticked in intake, even when the reference has no contact page): ikas has no `CONTACT` page type, contact section template or ready-made contact page, but the storefront ships a full contact form API, so every theme designs a custom `Contact` page (`pageType: CUSTOM`) that is sent to the ikas editor (studio) through the MCP. Design it as a full page, never a narrow centred form or a small two-column block: ContactForm + StoreLocator + FaqList (see the Contact row). API limits to respect: `submitContactForm` sends only first name, last name, email, phone, message (+ referer) and takes no files — a topic selector and an order-number field are allowed (the code prepends them to `message`), a file-upload field is not designed unless the brief names an external upload link. Channel cards follow rule 11: the value is the title (e-mail address, phone number), the hint goes below it, no small label above. Other custom pages are in scope only when the brief lists them. Each still uses Header + Footer and only Sections. Content-heavy policy pages use one rich-text Section rather than bespoke layouts.
