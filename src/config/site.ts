type ProfileLink = {
  label: string;
  href: string;
  icon: "github" | "instagram" | "email";
};

export const site: {
  name: string;
  title: string;
  description: string;
  profileImage: string;
  bio: string;
  location: string;
  links: ProfileLink[];
} = {
  name: "Eddie.Dev",
  title: "Eddie's TIL",
  description: "배운 것을 기록하고, 기록을 통해 성장하는 개발 TIL",
  profileImage: "https://github.com/EddieDawn.png?size=240",
  bio: "SSAFY 16th",
  location: "Suwon",
  links: [
    { label: "GitHub", href: "https://github.com/EddieDawn", icon: "github" },
    // 아래 URL의 `your-instagram-id`를 실제 Instagram 아이디로 바꾸세요.
    { label: "Instagram", href: "https://www.instagram.com/eddiedawn_/", icon: "instagram" },
    // 아래 이메일 주소를 실제 이메일 주소로 바꾸세요.
    { label: "Email", href: "mailto:autumnchristmas0613@gmail.com", icon: "email" },
  ],
};
