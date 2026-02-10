import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="미세먼지 산책 계산기", page_icon="🐶")

# 2. 우리가 만든 HTML/JS 코드 (GPT가 교정한 포커스 해제 로직 포함)
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { font-family: sans-serif; background: #f4f7f6; padding: 10px; display: flex; justify-content: center; }
        .card { background: white; padding: 20px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); width: 100%; max-width: 350px; border-top: 8px solid #ffcc00; }
        .header-tag { text-align: center; font-size: 0.8rem; color: #ff9900; font-weight: bold; margin-bottom: 5px; }
        h2 { color: #333; font-size: 1.4rem; margin: 0 0 20px 0; text-align: center; }
        label { display: block; margin-bottom: 5px; font-weight: bold; color: #555; font-size: 0.9rem; }
        select, input { width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 10px; border: 1px solid #ddd; font-size: 16px; box-sizing: border-box; }
        button { width: 100%; padding: 15px; background: #ffcc00; border: none; border-radius: 10px; font-weight: bold; font-size: 1.1rem; cursor: pointer; -webkit-appearance: none; }
        #result { margin-top: 20px; padding: 15px; background: #fff9e6; border-radius: 10px; font-weight: bold; color: #d35400; text-align: center; min-height: 50px; border: 1px dashed #ffcc00; word-break: keep-all; }
        .footer { margin-top: 20px; text-align: center; font-size: 0.8rem; color: #666; border-top: 1px solid #eee; padding-top: 10px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="header-tag">반려견 영양 오디오레터 [유료 구독자 전용]</div>
        <h2>🐶 산책 지수 계산기</h2>
        <label>우리 아이 상태</label>
        <select id="dogType">
            <option value="normal">일반 건강한 강아지</option>
            <option value="sensitive">민감군(단두종/노령견 등)</option>
        </select>
        <label>초미세먼지(PM2.5) 농도</label>
        <input type="number" id="pmValue" placeholder="숫자만 입력" inputmode="decimal">
        <button id="calcBtn">산책 확인하기</button>
        <div id="result">수치를 입력해 주세요!</div>
        <div class="footer"><b>반려견영양연구소 Dognutritionlab</b></div>
    </div>
    <script>
        document.getElementById('calcBtn').addEventListener('click', function () {
            var pmInput = document.getElementById('pmValue');
            var type = document.getElementById('dogType').value;
            var pm = Number(pmInput.value);
            var res = document.getElementById('result');
            pmInput.blur();
            if (!pmInput.value || isNaN(pm)) {
                res.innerHTML = "⚠️ 숫자를 입력해 주세요!";
                return;
            }
            var msg = "";
            if (type === 'sensitive') {
                if (pm <= 15) msg = "✅ 산책 가능!<br>(15~20분 권장)";
                else if (pm <= 25) msg = "⚠️ 주의!<br>10분 이내 퀵 산책";
                else msg = "❌ 산책 포기!<br>실내 활동 추천";
            } else {
                if (pm <= 15) msg = "✅ 산책하기 좋은 날!<br>(20~30분)";
                else if (pm <= 25) msg = "⚠️ 가벼운 산책<br>(15분 이내)";
                else if (pm <= 50) msg = "🚫 배변 산책만<br>(5분 이내)";
                else msg = "❌ 위험!<br>집에서 놀아주세요";
            }
            res.innerHTML = msg;
        });
    </script>
</body>
</html>
"""

# 3. 스트림릿 페이지에 HTML 삽입
components.html(html_code, height=600, scrolling=True)
