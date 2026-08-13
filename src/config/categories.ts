export const categories = [
  {
    slug: "java",
    name: "Java",
    description: "Java 문법, 객체지향 설계, Spring과 백엔드 개발 기록",
    accent: "#7a5c54",
  },
  {
    slug: "ai",
    name: "AI",
    description: "인공지능 개념, 모델 활용, 실험과 학습 기록",
    accent: "#6b778d",
  },
  {
    slug: "algorithm",
    name: "Algorithm",
    description: "문제 해결 과정과 알고리즘·자료구조 학습 기록",
    accent: "#65765f",
  },
] as const;

export type Category = (typeof categories)[number];
