# Components — kusurlu örnek

## 1. Sayfa → section bileşimi

| Sayfa (ikas sayfa tipi) | Referans URL | Section'lar (sırayla) |
|---|---|---|
| Ana sayfa (INDEX) | `/` | Hero · Ghost |
| Lookbook (LOOKBOOK) | `/lookbook` | Hero |

## 2. Section'lar

### Hero

| Prop | Tip | Varsayılan |
|---|---|---|
| `title` | TEXT | "Merhaba" |
| `heroImage` | IMAGE | hero.jpg |
| `Slide_count` | NUMBER | 3 |
| `autoplay` | BOOL | true |

### Footer
Prop: `columns` COMPONENT_LIST · `copyrightText` TXT.
