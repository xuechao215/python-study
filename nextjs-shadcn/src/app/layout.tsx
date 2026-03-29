import './globals.css'
import type { Metadata } from 'next'

// const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Next.js + shadcn',
  description: 'Starter with shadcn/ui'
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN" suppressHydrationWarning>
      <body className="antialiased min-h-screen bg-background font-sans">{children}</body>
    </html>
  )
}
