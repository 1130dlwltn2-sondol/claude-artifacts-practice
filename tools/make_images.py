#!/usr/bin/env python3
"""표지와 도식 이미지를 PIL로 생성한다. 크림 배경, Noto CJK 폰트."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT = Path.home() / "workspace" / "claude-artifacts-practice" / "assets"
BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

CREAM = (255, 246, 233)
INK = (31, 42, 68)
TEAL = (42, 161, 152)
CORAL = (232, 115, 74)
MUSTARD = (232, 180, 74)
LIGHT = (255, 255, 255)
GREY = (120, 128, 145)

def font(path, size):
    return ImageFont.truetype(path, size)

def cover():
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    # 상단 헤더
    d.text((80, 70), "WIKIDOCS TECH BOOK", font=font(BOLD, 34), fill=CORAL)
    d.line([(80, 120), (920, 120)], fill=(210, 190, 170), width=3)
    # 제목 (글자 영역)
    d.text((80, 170), "Claude로 문서·", font=font(BOLD, 88), fill=INK)
    d.text((80, 270), "슬라이드·대시보드", font=font(BOLD, 88), fill=INK)
    d.text((80, 370), "만들기", font=font(BOLD, 88), fill=TEAL)
    d.text((80, 490), "무료로 시작하는 문서 제작부터", font=font(REG, 36), fill=GREY)
    d.text((80, 540), "유료 베타 기능의 이해까지", font=font(REG, 36), fill=GREY)
    # 삽화 영역 (하단) - 친근한 플랫 스타일 도형
    d.rectangle([0, 660, W, H], fill=(240, 230, 214))
    # 문서
    d.rounded_rectangle([90, 760, 330, 1060], radius=24, fill=LIGHT, outline=INK, width=4)
    d.polygon([(270, 760), (330, 820), (270, 820)], fill=(225, 215, 198))
    for i, w in enumerate([180, 180, 180, 120]):
        d.rounded_rectangle([120, 880 + i * 45, 120 + w, 900 + i * 45], radius=8, fill=(215, 205, 190))
    # 슬라이드 덱
    d.rounded_rectangle([400, 800, 640, 940], radius=16, fill=CORAL)
    d.rounded_rectangle([415, 820, 625, 920], radius=12, fill=LIGHT)
    d.rounded_rectangle([430, 840, 560, 860], radius=6, fill=TEAL)
    d.rounded_rectangle([430, 872, 610, 884], radius=6, fill=(215, 205, 190))
    d.rounded_rectangle([430, 892, 590, 904], radius=6, fill=(215, 205, 190))
    d.rounded_rectangle([390, 950, 630, 1080], radius=16, fill=(255, 252, 246), outline=INK, width=3)
    d.text((455, 1000), "5장", font=font(BOLD, 40), fill=INK)
    # 대시보드
    d.rounded_rectangle([700, 760, 930, 1060], radius=24, fill=INK)
    for i, h in enumerate([80, 130, 100, 160]):
        x = 730 + i * 50
        d.rounded_rectangle([x, 1000 - h, x + 34, 1000], radius=8, fill=TEAL if i % 2 == 0 else MUSTARD)
    d.text((730, 920), "가상 지표", font=font(REG, 26), fill=LIGHT)
    # 재생 버튼 (모션)
    d.ellipse([440, 1085, 560, 1205], fill=MUSTARD, outline=INK, width=4)
    d.polygon([(480, 1110), (480, 1180), (535, 1145)], fill=INK)
    # 하단 저자
    d.text((80, 1180 - 60), "저자 이준수", font=font(REG, 32), fill=GREY)
    d.text((80, 1180 - 20), "기준일 2026-10-10", font=font(REG, 32), fill=GREY)
    img.save(ROOT / "cover.png")
    print("cover.png", img.size)

def plan_matrix():
    W, H = 1200, 780
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.text((60, 40), "플랜별 기능 가용성 (2026-10-10 기준, 모식도)", font=font(BOLD, 40), fill=INK)
    cols = ["기능", "Free", "Pro", "Max", "Team", "Enterprise"]
    rows = [
        ("대화에서 결과물 만들기", ["됨", "됨", "됨", "됨", "됨"]),
        ("Docs·Slides·Design", ["됨", "됨", "됨", "됨", "됨"]),
        ("Dashboards (베타)", ["안 됨", "됨", "됨", "됨", "됨"]),
        ("Motion (베타)", ["안 됨", "안 됨", "안 됨", "됨", "됨"]),
    ]
    x0, y0 = 60, 140
    cw = [380, 140, 140, 140, 140, 140]
    rh = 100
    for j, c in enumerate(cols):
        x = x0 + sum(cw[:j])
        d.rectangle([x, y0, x + cw[j], y0 + rh], fill=INK)
        d.text((x + 20, y0 + 28), c, font=font(BOLD, 32), fill=LIGHT)
    for i, (label, vals) in enumerate(rows):
        y = y0 + rh * (i + 1)
        bg = LIGHT if i % 2 == 0 else (248, 240, 226)
        x = x0
        d.rectangle([x, y, x + cw[0], y + rh], fill=bg, outline=(210, 190, 170), width=2)
        d.text((x + 20, y + 28), label, font=font(REG, 30), fill=INK)
        for j, v in enumerate(vals):
            x = x0 + sum(cw[: j + 1])
            d.rectangle([x, y, x + cw[j], y + rh], fill=bg, outline=(210, 190, 170), width=2)
            col = TEAL if v == "됨" else (CORAL if v == "안 됨" else INK)
            d.text((x + 30, y + 28), v, font=font(BOLD, 30), fill=col)
    d.text((60, 660), "실제 제품 화면이 아닌 모식도입니다. 최신 정보는 공식 도움말에서 확인하세요.",
           font=font(REG, 26), fill=GREY)
    img.save(ROOT / "plan-matrix.png")
    print("plan-matrix.png", img.size)

def dashboard_spec():
    W, H = 1200, 900
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.text((60, 40), "대시보드 명세서의 구성 (모식도)", font=font(BOLD, 42), fill=INK)
    boxes = [
        ("지표 정의", "매출이 무엇인지 정한다\n예: 취소 제외, 부가세 포함", TEAL),
        ("계산식", "평균객단가 = 매출 합계 /\n주문 합계", CORAL),
        ("갱신 주기", "언제 기준으로\n업데이트되는지", MUSTARD),
        ("오류 검증표", "숫자가 안 맞을 때\n확인할 순서", INK),
    ]
    for i, (t, desc, col) in enumerate(boxes):
        x = 60 + i * 275
        d.rounded_rectangle([x, 160, x + 245, 560], radius=20, fill=LIGHT, outline=col, width=5)
        d.rounded_rectangle([x, 160, x + 245, 240], radius=20, fill=col)
        d.rectangle([x, 220, x + 245, 240], fill=col)
        d.text((x + 30, 178), t, font=font(BOLD, 32), fill=LIGHT)
        d.text((x + 24, 280), desc, font=font(REG, 28), fill=INK)
        if i < 3:
            cx = x + 245
            d.polygon([(cx + 5, 340), (cx + 5, 380), (cx + 30, 360)], fill=GREY)
    d.rounded_rectangle([60, 640, 1140, 780], radius=16, fill=(240, 230, 214))
    d.text((90, 680), "명세서가 정확해야 대시보드가 정확합니다. 지표 정의와 출처를 먼저 연결하세요.",
           font=font(REG, 30), fill=INK)
    d.text((60, 820), "실제 제품 화면이 아닌 모식도입니다.", font=font(REG, 26), fill=GREY)
    img.save(ROOT / "dashboard-spec.png")
    print("dashboard-spec.png", img.size)

def storyboard():
    W, H = 1400, 760
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.text((60, 40), "20초 애니메이션 스토리보드 6컷 (모식도)", font=font(BOLD, 42), fill=INK)
    cuts = [
        ("컷 1", "0~4초", "제목 화면", "사실"),
        ("컷 2", "4~7초", "9월 1일 38건", "사실"),
        ("컷 3", "7~11초", "9월 5일 52건 최고", "사실"),
        ("컷 4", "11~14초", "9월 10일 40건", "사실"),
        ("컷 5", "14~17초", "원인: 점검 2시간", "사실"),
        ("컷 6", "17~20초", "10월 회복 예상", "가정"),
    ]
    for i, (c, t, desc, tag) in enumerate(cuts):
        x = 60 + i * 215
        col = TEAL if tag == "사실" else CORAL
        d.rounded_rectangle([x, 140, x + 195, 560], radius=16, fill=LIGHT, outline=col, width=4)
        d.text((x + 20, 160), c, font=font(BOLD, 32), fill=INK)
        d.text((x + 20, 210), t, font=font(REG, 26), fill=GREY)
        d.text((x + 20, 260), desc, font=font(REG, 28), fill=INK)
        d.rounded_rectangle([x + 20, 460, x + 110, 510], radius=12, fill=col)
        d.text((x + 34, 470), tag, font=font(BOLD, 26), fill=LIGHT)
    d.text((60, 620), "각 컷에 사실/가정을 표시합니다. 실제 제품 화면이 아닌 모식도입니다.",
           font=font(REG, 28), fill=GREY)
    d.text((60, 670), "수치는 모두 가상입니다.", font=font(REG, 28), fill=GREY)
    img.save(ROOT / "motion-storyboard.png")
    print("motion-storyboard.png", img.size)

if __name__ == "__main__":
    ROOT.mkdir(parents=True, exist_ok=True)
    cover()
    plan_matrix()
    dashboard_spec()
    storyboard()
