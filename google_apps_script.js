// ╔══════════════════════════════════════════════════════════════╗
// ║        FIDELUP — Google Apps Script (Backend Leads)         ║
// ║  Copia TUTTO questo codice in Google Apps Script            ║
// ║  script.google.com → Nuovo progetto → incolla qui          ║
// ╚══════════════════════════════════════════════════════════════╝

// ─── STEP 1: Sostituisci con il tuo Spreadsheet ID ─────────────
// Apri il tuo Google Sheet e prendi l'ID dall'URL:
// https://docs.google.com/spreadsheets/d/ [[ QUESTO ]] /edit
const SHEET_ID = '1zMp46PwbpzKSFn55ggWrHUEeSHjyq-VwDW1TZwCpVoo';

// ─── STEP 2: Nome del tab/foglio dove salvare i dati ───────────
const SHEET_NAME = 'Lead FidelUp';

// ───────────────────────────────────────────────────────────────
//  doPost — viene chiamato dal form della landing page
//  Riceve: nome, attivita, telefono, citta, source, timestamp
// ───────────────────────────────────────────────────────────────
function doPost(e) {
  try {
    // Parsa il JSON inviato dal form
    const raw  = e.postData ? e.postData.contents : '{}';
    const data = JSON.parse(raw);

    const ss    = SpreadsheetApp.openById(SHEET_ID);
    let   sheet = ss.getSheetByName(SHEET_NAME);

    // Crea il foglio se non esiste
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
    }

    // ── Prima riga: intestazioni colorate ──────────────────────
    if (sheet.getLastRow() === 0) {
      const headers = [
        '📅 Data e Ora',
        '👤 Nome e Cognome',
        '🏪 Nome Attività',
        '📱 Telefono',
        '📍 Città',
        '✅ Privacy',
        '🔖 Fonte',
        '⏱️ Timestamp ISO'
      ];
      sheet.appendRow(headers);

      // Stile intestazioni
      const hRange = sheet.getRange(1, 1, 1, headers.length);
      hRange.setFontWeight('bold')
            .setBackground('#2E7D32')
            .setFontColor('#FFFFFF')
            .setFontSize(11);
      sheet.setFrozenRows(1);

      // Larghezze colonne
      sheet.setColumnWidth(1, 140);
      sheet.setColumnWidth(2, 180);
      sheet.setColumnWidth(3, 200);
      sheet.setColumnWidth(4, 130);
      sheet.setColumnWidth(5, 130);
      sheet.setColumnWidth(6,  80);
      sheet.setColumnWidth(7, 180);
      sheet.setColumnWidth(8, 180);
    }

    // ── Formato data leggibile in italiano ─────────────────────
    const ora = new Date().toLocaleString('it-IT', {
      timeZone:  'Europe/Rome',
      day:       '2-digit',
      month:     '2-digit',
      year:      'numeric',
      hour:      '2-digit',
      minute:    '2-digit'
    });

    // ── Aggiungi riga con i dati ricevuti ──────────────────────
    const newRow = [
      ora,
      (data.nome        || '').trim(),
      (data.attivita    || '').trim(),
      (data.telefono    || '').trim(),
      (data.citta       || '').trim(),
      data.privacy_consent === 'si' ? '✅ Sì' : '❌ No',
      data.source       || 'FidelUp Landing Page',
      data.timestamp    || new Date().toISOString()
    ];

    sheet.appendRow(newRow);

    // ── Colora righe alternate per leggibilità ─────────────────
    const lastRow = sheet.getLastRow();
    if (lastRow % 2 === 0) {
      sheet.getRange(lastRow, 1, 1, newRow.length).setBackground('#F1F8E9');
    }

    // ── Risposta OK ────────────────────────────────────────────
    return buildResponse({ status: 'ok', lead: data.nome || 'anonimo' });

  } catch (err) {
    return buildResponse({ status: 'error', message: err.toString() });
  }
}

// ───────────────────────────────────────────────────────────────
//  doGet — per test manuali nell'URL del browser
// ───────────────────────────────────────────────────────────────
function doGet(e) {
  return buildResponse({
    status:  'ok',
    service: 'FidelUp Lead Collector',
    info:    'Invia una richiesta POST con i dati del form'
  });
}

// ───────────────────────────────────────────────────────────────
//  Helper — risposta JSON con header CORS
// ───────────────────────────────────────────────────────────────
function buildResponse(obj) {
  const output = ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
  return output;
}

// ───────────────────────────────────────────────────────────────
//  TEST MANUALE — Esegui questa funzione dentro Apps Script
//  per verificare che il foglio funzioni prima di fare deploy
// ───────────────────────────────────────────────────────────────
function testInserisciLead() {
  const fakeEvent = {
    postData: {
      contents: JSON.stringify({
        nome:            'Mario Rossi (TEST)',
        attivita:        'Bar Centrale',
        telefono:        '333 123 4567',
        citta:           'Milano',
        privacy_consent: 'si',
        source:          'TEST manuale',
        timestamp:       new Date().toISOString()
      })
    }
  };
  const result = doPost(fakeEvent);
  Logger.log(result.getContent());
}
