const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://www.instagram.com/');

  // Aguarda até que os campos de entrada de usuário e senha estejam prontos para uso
  await page.waitForSelector('input[name="username"]');
  await page.waitForSelector('input[name="password"]');
  await page.waitForSelector('button[type="submit"]');

  // Insira suas credenciais aqui
  const username = 'seyzalel';
  const password = 'Sey17zalel17@$';

  // Insere o usuário e a senha
  await page.type('input[name="username"]', username);
  await page.type('input[name="password"]', password);

  // Aguarda até que o botão de login esteja habilitado
  await page.waitForFunction(() => !document.querySelector('button[type="submit"]').hasAttribute('disabled'));

  // Clica no botão de login
  await page.click('button[type="submit"]');

  // Aguarda o redirecionamento após o login
  await page.waitForNavigation();

  // Verifica se a URL de redirecionamento contém 'accounts' ou 'onetap'
  const redirectedURL = page.url();
  if (redirectedURL.includes('accounts') || redirectedURL.includes('onetap')) {
    // Insira as ações adicionais necessárias após o login, como navegar para uma determinada página
    console.log("Login bem-sucedido!");
  } else {
    console.log("URL de redirecionamento desconhecida após o login.");
  }

  // Fecha o navegador após a conclusão
  await browser.close();
})();