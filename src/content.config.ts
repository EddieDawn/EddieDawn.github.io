import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

const posts = defineCollection({
  // src/content/posts 아래의 Markdown 파일을 모두 TIL 게시물로 읽습니다.
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  // 각 글의 맨 위(frontmatter)에 반드시 있어야 할 최소 정보를 정의합니다.
  schema: z.object({
    title: z.string(),
    publishedAt: z.coerce.date(),
  }),
});

export const collections = { posts };
