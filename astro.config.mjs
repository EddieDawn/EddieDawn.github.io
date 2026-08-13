import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
    server: {
      watch: {
        // Windows 폴더를 Docker Linux 컨테이너에 마운트하면 파일 변경 이벤트가
        // 전달되지 않을 수 있어, 주기적으로 변경을 확인하는 방식을 사용합니다.
        usePolling: true,
        interval: 300,
      },
    },
  },
});
