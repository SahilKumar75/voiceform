const FIELD_LABELS = {
  applicant_name: { en: 'Name', hi: 'नाम' },
  date_of_birth: { en: 'Date of Birth', hi: 'जन्म तिथि' },
  state_of_domicile: { en: 'State', hi: 'राज्य' },
  community_category: { en: 'Category', hi: 'श्रेणी' },
  annual_family_income: { en: 'Annual Income', hi: 'वार्षिक आय' },
  bank_account_number: { en: 'Bank Account', hi: 'बैंक खाता' },
  bank_ifsc_code: { en: 'IFSC Code', hi: '' },
};

const DEMO_VALUES = {
  applicant_name: 'Ravi Kumar',
  date_of_birth: '14-08-2007',
  state_of_domicile: 'Bihar',
  community_category: 'OBC',
  annual_family_income: '₹1,20,000',
  bank_account_number: '3021 4455 6698',
  bank_ifsc_code: 'SBIN0001234',
};

const fieldList = document.getElementById('fieldList');
const micButton = document.getElementById('micButton');
const micStatus = document.getElementById('micStatus');

let fieldOrder = [];

fetch('../schema.json')
  .then((res) => res.json())
  .then((schema) => {
    fieldOrder = schema.required;
    renderFields();
  })
  .catch(() => {
    fieldOrder = Object.keys(FIELD_LABELS);
    renderFields();
  });

function renderFields() {
  fieldList.innerHTML = '';
  fieldOrder.forEach((key) => {
    const label = FIELD_LABELS[key] || { en: key, hi: '' };
    const li = document.createElement('li');
    li.className = 'field-row';
    li.dataset.field = key;
    li.innerHTML = `
      <span class="field-label">${label.en}${label.hi ? ' / ' + label.hi : ''}</span>
      <span class="field-value"><span class="field-check">&#10003;</span><span class="field-text">not filled yet</span></span>
    `;
    fieldList.appendChild(li);
  });
}

let demoRunning = false;

micButton.addEventListener('click', () => {
  if (demoRunning) return;
  demoRunning = true;
  micStatus.textContent = 'Listening / सुन रहा है...';

  let i = 0;
  const rows = Array.from(fieldList.querySelectorAll('.field-row'));
  const interval = setInterval(() => {
    if (i >= rows.length) {
      clearInterval(interval);
      micStatus.textContent = 'Done / पूरा हुआ';
      setTimeout(() => {
        rows.forEach((row) => {
          row.classList.remove('is-filled');
          row.querySelector('.field-text').textContent = 'not filled yet';
        });
        micStatus.textContent = 'Tap to speak / बोलने के लिए टैप करें';
        demoRunning = false;
      }, 1800);
      return;
    }
    const row = rows[i];
    const key = row.dataset.field;
    row.querySelector('.field-text').textContent = DEMO_VALUES[key] || '...';
    row.classList.add('is-filled');
    i += 1;
  }, 450);
});
