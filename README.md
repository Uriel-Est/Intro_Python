# Introdução aos Softwares Estatísticos — Site (Quarto)

Este repositório publica uma página estilo **site** (Quarto) para um relatório sobre **Quarto**, **Git/GitHub**, **pip** e conceitos básicos de **Python**.

## O que tem aqui

- **`index.qmd`** — página principal (TOC à direita, sem sidebar de projeto).
- **`_quarto.yml`** — configuração do site (output em `docs/` e navbar).
- **`styles.css`** — visual custom (navbar com imagem de fundo + logos).
- **`toc-fix.css`** — correção para o TOC da margem **não** herdar o estilo da classe `.sidebar`.
- **`background.png`, `LOGO-PNG³.png`, `logo-dept.png`, `logo-uf.png`** — imagens do header.
- **`README.md`** — este guia.

> Outros arquivos úteis que podem existir: `_header.html`, `_margins.html`, `_sidebar.html` (includes do Quarto) e `_custom.scss` (ajustes SASS).

## Como rodar

Pré-requisitos: [Quarto](https://quarto.org) instalado e **Python** acessível (se for executar os blocos `{python}`).

```bash
# preview do site (no diretório do projeto)
quarto preview --no-browser

# build final (gera docs/)
quarto render
```

A saída do site fica na pasta **`docs/`**, pronta para **GitHub Pages**.

## Publicar no GitHub Pages

1. Faça `git push` para o GitHub (branch `main`).
2. No repositório → **Settings → Pages**:
   - **Source**: *Deploy from branch*
   - **Branch**: `main`
   - **Folder**: `/docs`
3. Aguarde o deploy e acesse a URL indicada pelo GitHub.

## Estrutura típica 🗂️

```
.
├─ docs/                     # build final (HTML/CSS/JS) — versionado (GitHub Pages)
├─ index.qmd                 # conteúdo principal
├─ _quarto.yml               # config do site
├─ styles.css                # seu tema custom
├─ toc-fix.css               # patch: TOC da margem transparente/compacto
├─ background.png            # imagem do header
├─ LOGO-PNG³.png             # logos do header
├─ logo-dept.png
├─ logo-uf.png
└─ README.md
```

> **Nota:** para evitar conflitos, `.gitignore` ignora `_site/` e `.quarto/` (cache/intermediários), e mantém **`docs/`** versionado (é de onde o Pages serve).

## Como editar os assuntos sem “bagunçar”

- **Mantenha IDs estáveis** nas seções do `index.qmd` usando `{#meu-id}` nos títulos. Ex.: `## Git e GitHub {#git-e-github}`.
- **Use apenas headings (`#`, `##`, `###`)** para estruturar. Nada de inventar `div`s desnecessárias.
- **TOC à direita**: garantido por `toc: true` + `toc-location: right` no front matter do `index.qmd`.
- **Não reestilize `.sidebar` globalmente** no CSS — essa classe é usada pelo **TOC da margem**. No `styles.css` os estilos da sidebar do projeto estão **escopados** por `#quarto-sidebar` e `body.nav-sidebar`.  
  - Se precisar mexer no TOC, faça isso via `#quarto-margin-sidebar` (como em `toc-fix.css`).

### Adicionar/alterar tópicos

1. Edite o `index.qmd`:
   - Copie um bloco de seção existente.
   - Ajuste o título e o conteúdo.
   - Dê um **ID único** `{#seu-topico}`.
2. Se quiser **outras páginas** (ex.: `python.qmd`, `git.qmd`):
   - Crie o arquivo `.qmd`.
   - Inclua na navbar em `_quarto.yml`:
     ```yaml
     website:
       navbar:
         left:
           - text: "Início"
             href: index.qmd
           - text: "Python"
             href: python.qmd
     ```
   - Opcional: adicione também em `project.render`.

### Includes opcionais (avançado)
- `/_header.html`, `/_margins.html`, `/_sidebar.html`: permitem customizar trechos do HTML. Se usar, aponte em `_quarto.yml`:
  ```yaml
  format:
    html:
      include-in-header: _header.html      # CSS/JS extras
      include-before-body: _margins.html   # margens/TOC custom
      include-after-body: _sidebar.html    # blocos no fim
  ```

## O que já corrigimos (evitar bugs comuns) 🦆

- **TOC virando “caixa branca”**: era o CSS global em `.sidebar`.  
  - Solução: escopar estilos **só** para `#quarto-sidebar` (sidebar do projeto) e **proteger** `#quarto-margin-sidebar` no `toc-fix.css`.
- **Fenced div `:::` mal-fechada**: exemplos de código com blocos dentro de blocos agora usam **quatro crases** (````) no `index.qmd`.
- **Header sumindo**: lembrando que o **navbar só aparece quando roda como `website`** (use `_quarto.yml` e `quarto preview` no projeto).  
  Para arquivo único utilize `title-block-banner`.

## Git — fluxo rápido

```bash
quarto render                     # gera docs/
git add -A
git commit -m "site: conteúdo e estilo atualizados"
git push -u origin main
```

Se surgir erro com “sub-repo” (ex.: `does not have a commit checked out`), é pasta com `.git` dentro do repo. Remova o `.git` interno **ou** ignore a pasta no `.gitignore` e faça `git rm -r --cached <pasta>`.

## Personalização do header 🖼️

- As imagens estão no `styles.css` como `background: url('background.png')` etc.  
- Troque as imagens mantendo o mesmo nome **ou** altere o caminho no CSS.
- Ajustes de tamanho estão nas media queries (`@media`), já prontos.

