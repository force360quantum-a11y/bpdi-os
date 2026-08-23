from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

bad = "Conteúdo integral preservado para rastreabilidade. A seção 'ATUALIZAÇÃO CANÔNICA V3' prevalece sobre formulações históricas incompatíveis."
good = "Conteúdo integral preservado para rastreabilidade. A seção ATUALIZAÇÃO CANÔNICA V3 prevalece sobre formulações históricas incompatíveis."
if bad in s:
    s = s.replace(bad, good, 1)
elif good not in s:
    raise SystemExit('Texto do Documento Fundacional não encontrado')

old = """// Gate and boot
$('#confidentialAgree').onchange=e=>$('#enterApp').disabled=!e.target.checked;
$('#enterApp').onclick=async()=>{const stored=localStorage.getItem('bpdi_pin_hash');if(stored){const pin=prompt('Digite o PIN local:');if(await sha256(pin||'')!==stored){toast('PIN incorreto');return}}localStorage.setItem('bpdi_confidential_accept','1');$('#confidentialGate').classList.add('hidden');render('dashboard')};
const accepted=localStorage.getItem('bpdi_confidential_accept')==='1'; const hasPin=!!localStorage.getItem('bpdi_pin_hash'); if(accepted&&!hasPin){$('#confidentialGate').classList.add('hidden')}else if(hasPin){$('#confidentialAgree').checked=true;$('#enterApp').disabled=false}
"""
new = """// Gate and boot — V3.0.1
const agreeBox=$('#confidentialAgree');
const enterBtn=$('#enterApp');
function syncGateButton(){if(agreeBox&&enterBtn)enterBtn.disabled=!agreeBox.checked}
agreeBox?.addEventListener('change',syncGateButton);
agreeBox?.addEventListener('input',syncGateButton);
window.addEventListener('pageshow',syncGateButton);
setTimeout(syncGateButton,0);
enterBtn?.addEventListener('click',async()=>{
  if(!agreeBox?.checked){syncGateButton();return}
  const stored=localStorage.getItem('bpdi_pin_hash');
  if(stored){
    const pin=prompt('Digite o PIN local:');
    if(await sha256(pin||'')!==stored){toast('PIN incorreto');return}
  }
  localStorage.setItem('bpdi_confidential_accept','1');
  $('#confidentialGate')?.classList.add('hidden');
  render('dashboard');
});
const accepted=localStorage.getItem('bpdi_confidential_accept')==='1';
const hasPin=!!localStorage.getItem('bpdi_pin_hash');
if(accepted&&!hasPin){$('#confidentialGate')?.classList.add('hidden')}
else if(hasPin){agreeBox.checked=true;syncGateButton()}
"""
if old in s:
    s = s.replace(old, new, 1)
elif '// Gate and boot — V3.0.1' not in s:
    raise SystemExit('Bloco do gate não encontrado')

s = s.replace('Versão 3.0.0 · agosto/2026 · dados no navegador', 'Versão 3.0.1 · agosto/2026 · dados no navegador', 1)
s = s.replace('"version":"3.0.0","generated":"2026-08-23"', '"version":"3.0.1","generated":"2026-08-23"', 1)

p.write_text(s, encoding='utf-8')
print('V3 runtime repaired')
