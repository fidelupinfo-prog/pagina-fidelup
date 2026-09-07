// ╔══════════════════════════════════════════════════════════════╗
// ║   FIDELUP — Google Apps Script (Backend Landing Page + Quiz) ║
// ║  Copia TUTTO questo codice in Google Apps Script             ║
// ║  script.google.com → Nuovo progetto → incolla qui           ║
// ╚══════════════════════════════════════════════════════════════╝

const SHEET_ID = '1zMp46PwbpzKSFn55ggWrHUEeSHjyq-VwDW1TZwCpVoo';

function doPost(e) {
  try {
    const raw = e.postData ? e.postData.contents : '{}';
    const data = JSON.parse(raw);

    const ss = SpreadsheetApp.openById(SHEET_ID);
    const source = data.source || 'FidelUp Landing Page';

    // Riconosce automaticamente se il lead viene dal Quiz o dalla Landing Page
    const isQuiz = source.includes("Quiz");

    const SHEET_NAME = isQuiz ? 'Lead Quiz' : 'Lead FidelUp';
    let sheet = ss.getSheetByName(SHEET_NAME);

    // Crea il foglio specifico se non esiste
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
    }

    // Imposta intestazioni in base a da dove arriva il contatto
    if (sheet.getLastRow() === 0) {
      let headers = [];
      if (isQuiz) {
        headers = ['📅 Data e Ora', '👤 Nome e Cognome', '🏪 Nome Attività', '📱 Tipo Contatto', '🔗 Contatto', '🎯 Profilo Risultato', '✅ Privacy', '🔖 Fonte', '⏱️ Timestamp ISO'];
      } else {
        headers = ['📅 Data e Ora', '👤 Nome e Cognome', '🏪 Nome Attività', '📱 Telefono', '📍 Città', '✅ Privacy', '🔖 Fonte', '⏱️ Timestamp ISO'];
      }
      sheet.appendRow(headers);

      const hRange = sheet.getRange(1, 1, 1, headers.length);
      hRange.setFontWeight('bold').setBackground('#2E7D32').setFontColor('#FFFFFF').setFontSize(11);
      sheet.setFrozenRows(1);
    }

    const ora = new Date().toLocaleString('it-IT', { timeZone: 'Europe/Rome', day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' });

    // Prepara la riga in base a dove arriva il lead
    let newRow = [];
    if (isQuiz) {
      newRow = [
        ora,
        (data.nome || '').trim(),
        (data.attivita || '').trim(),
        (data.contatto_tipo || '').trim(),
        (data.contatto_valore || '').trim(),
        (data.profilo_risultato || '').trim(),
        data.privacy_consent === 'si' ? '✅ Sì' : '❌ No',
        source,
        data.timestamp || new Date().toISOString()
      ];
    } else {
      newRow = [
        ora,
        (data.nome || '').trim(),
        (data.attivita || '').trim(),
        (data.telefono || '').trim(),
        (data.citta || '').trim(),
        data.privacy_consent === 'si' ? '✅ Sì' : '❌ No',
        source,
        data.timestamp || new Date().toISOString()
      ];
    }

    sheet.appendRow(newRow);

    // Stile a righe alterne
    const lastRow = sheet.getLastRow();
    if (lastRow % 2 === 0) {
      sheet.getRange(lastRow, 1, 1, newRow.length).setBackground('#F1F8E9');
    }

    return ContentService.createTextOutput(JSON.stringify({ status: 'ok', type: isQuiz ? 'quiz' : 'landing' })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: err.toString() })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({ status: 'ok', service: 'FidelUp Lead Collector' })).setMimeType(ContentService.MimeType.JSON);
}
