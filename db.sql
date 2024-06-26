USE [master]
GO
/****** Object:  Database [QLSV]    Script Date: 6/24/2024 6:08:28 PM ******/
CREATE DATABASE [QLSV]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'QLSV', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\QLSV.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'QLSV_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\QLSV_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [QLSV] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [QLSV].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [QLSV] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [QLSV] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [QLSV] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [QLSV] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [QLSV] SET ARITHABORT OFF 
GO
ALTER DATABASE [QLSV] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [QLSV] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [QLSV] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [QLSV] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [QLSV] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [QLSV] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [QLSV] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [QLSV] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [QLSV] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [QLSV] SET  DISABLE_BROKER 
GO
ALTER DATABASE [QLSV] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [QLSV] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [QLSV] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [QLSV] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [QLSV] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [QLSV] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [QLSV] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [QLSV] SET RECOVERY FULL 
GO
ALTER DATABASE [QLSV] SET  MULTI_USER 
GO
ALTER DATABASE [QLSV] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [QLSV] SET DB_CHAINING OFF 
GO
ALTER DATABASE [QLSV] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [QLSV] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [QLSV] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [QLSV] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'QLSV', N'ON'
GO
ALTER DATABASE [QLSV] SET QUERY_STORE = ON
GO
ALTER DATABASE [QLSV] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [QLSV]
GO
/****** Object:  Table [dbo].[Diem]    Script Date: 6/24/2024 6:08:28 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Diem](
	[maSinhVien] [varchar](255) NOT NULL,
	[maMonHoc] [varchar](10) NOT NULL,
	[diem] [decimal](4, 2) NULL,
 CONSTRAINT [PK__Diem__702633A64331B4F7] PRIMARY KEY CLUSTERED 
(
	[maSinhVien] ASC,
	[maMonHoc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[MonHoc]    Script Date: 6/24/2024 6:08:28 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MonHoc](
	[maMonHoc] [varchar](10) NOT NULL,
	[tenMonHoc] [varchar](255) NULL,
PRIMARY KEY CLUSTERED 
(
	[maMonHoc] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[SinhVien]    Script Date: 6/24/2024 6:08:28 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[SinhVien](
	[maSinhVien] [varchar](255) NOT NULL,
	[tenSinhVien] [varchar](255) NULL,
	[lop] [varchar](255) NULL,
 CONSTRAINT [PK__SinhVien__D9B6EE60184D7298] PRIMARY KEY CLUSTERED 
(
	[maSinhVien] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[Diem] ([maSinhVien], [maMonHoc], [diem]) VALUES (N'1', N'001', CAST(7.00 AS Decimal(4, 2)))
INSERT [dbo].[Diem] ([maSinhVien], [maMonHoc], [diem]) VALUES (N'1', N'003', CAST(9.00 AS Decimal(4, 2)))
INSERT [dbo].[Diem] ([maSinhVien], [maMonHoc], [diem]) VALUES (N'1', N'004', CAST(10.00 AS Decimal(4, 2)))
INSERT [dbo].[Diem] ([maSinhVien], [maMonHoc], [diem]) VALUES (N'2', N'001', CAST(8.00 AS Decimal(4, 2)))
INSERT [dbo].[Diem] ([maSinhVien], [maMonHoc], [diem]) VALUES (N'2', N'003', CAST(8.00 AS Decimal(4, 2)))
INSERT [dbo].[Diem] ([maSinhVien], [maMonHoc], [diem]) VALUES (N'2', N'004', CAST(7.00 AS Decimal(4, 2)))
INSERT [dbo].[Diem] ([maSinhVien], [maMonHoc], [diem]) VALUES (N'3', N'005', CAST(6.00 AS Decimal(4, 2)))
GO
INSERT [dbo].[MonHoc] ([maMonHoc], [tenMonHoc]) VALUES (N'001', N'CTDLVGT')
INSERT [dbo].[MonHoc] ([maMonHoc], [tenMonHoc]) VALUES (N'002', N'Toan Cao Cap')
INSERT [dbo].[MonHoc] ([maMonHoc], [tenMonHoc]) VALUES (N'003', N'He quan tri CSDL')
INSERT [dbo].[MonHoc] ([maMonHoc], [tenMonHoc]) VALUES (N'004', N'.NET')
INSERT [dbo].[MonHoc] ([maMonHoc], [tenMonHoc]) VALUES (N'005', N'Java')
GO
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'1', N'J9W1P4t4Nn7Is5IgBVWBnNKkH5WCKrOU8qBFsbatqFrAA4yUkgHgtJWSck0qN0E=', N'FQBGgd+JKBbGbTyzMMHS8lGg/lNc0DVcAAH1ENdXH54PpdMaug==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'10', N'EJDehq1IBkzTUDAHeoN4jEmGrJrV+ZZ3nUCNFQvWMmmEX5pf6OCPXrK5LlfMShT1', N'4bjsQazVRhLGaGn5erK73ED6Nz0GZqZqSJTw+5TzDbkaYo44Ow==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'11', N'vMvZU7V2Bj4y3yX/9lm/VD6rYwFNkwnbmZCyx/Fagyvm4D3Rms0CU/Ct2OnRkSca', N'ihwZ1zrCygZsKFg8zgsuT16ztbm/EK2cez3Cn1rRRky01Pl0qg==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'12', N'nyXMr3OEByV1oOyX62m6t8FvIor9YtO6Bf6zP7PFV2l19csuAb9FBj4zQxUIvse5', N'6JHY0kzskg/ILxcNGgOs3pfUQY6GlAaFxTr2bDm3IbcKavKZPw==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'13', N'TS6jqTBICj9C709Mc5YQ85wUmnj9b1KAMCBmZW4cz9ZrHJIVcur/r4u5lNa9+xt6', N'xrpYPEovZGwCAWRMEKcE2HSiybK/+1UVR5nlRrG3rsKpQIqPdQ==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'14', N'ZzjqEb9Xp51YfqYUU5A6IKZ6mTUllAVb3FRkytnhEWxtZTT1ShzgY8jcd3KWAPqN', N'YqgqLG3piBnPwA2fvDaN80E2QJcYpmKU9t5VF2HLx4tYHmb2VQ==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'15', N'dYH3CgWyrNzYSCEWOTDvQUIUY4567YpIrzYOBDLeBsaIqtNDwJpOqS98L/QF4T29', N'XLNzVO8au+yzMSXvseHw0xLI2T/e86IwSHhlw7PJ6Tsb/BZ40Q==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'16', N'ra3y4eAor8iLLxMSWzZ3TkTEr2h4SU90yCy83SMfEXEVJsq0NURTLbg4Qn4yTfVw', N'MY730aN3KnTqyHMGC2upjfvgWkDCrxGuLmV+iAwhAK330wzxhg==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'17', N'RbUKYGf2boGRJVt7ZD9qHcGop+ZsYpufoESo3kh4eXkSF8FH7Gx1VZS6PfZYW7HP', N'OTaTJq9GAu0/s47Lt4rO2dLo+zjYxST7314UYB0kYMwxHdfmkQ==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'18', N'WKM6BaBl6xy0rZF9KgYv1MZhaOncfNk24LgJdZSjMFrNOACh4ifkVZeAfiPDcjBn', N'4vrbfaMkIlqwtKYhB0qb9tHR6wNCYhB41VMvrike15GRtXaIdg==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'19', N'/g5vY+un67fMBoG4uz3LOBIedbrsab3XArCCbHQXGYVx3qZsNCN/A+FmJTb9ZtZu', N'AAQCk4RffM6XpRmY74mQ0x2NFK7bQenVL3aXqKunjD80P/J1kQ==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'2', N's8YQbJwNMf33bGXO67GhUcdA2R8ntOeh+TpPrDj43FjRNj+mlpDIXAgyPQGqzh8=', N'GDI5/Wd95NlNiOxMs9514OMJVgtscFrUxskehRz5WoL7Mbtoow==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'20', N'uNyX1JazG9oddk+0DvW2BdVFTKX8iYjkR3pKTTZq/Aiq+ERkvXmWf1ZyqF7WW45E', N'MCF/oX/Lp3mjShRAriy0E73bVJdp8pFv3FGT3sR3O8Z5W94cng==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'3', N'cNPbhm8sH/Bw2b5k7dKm0TuJv1+C88TufYuzPwXSbqIewMPmB6uQZPDYE2Y12iA=', N'Ps0Et89UW8gOKZVGyLGe87QPh72vaDABlgEOMIgkq3UFFxEFpg==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'4', N'3+hfg3SaU3Fk9zQPakm9hC13UybcVwqTPax72Dc0/PLY5JmNA0btqWeUPNTbo24=', N'QBzWGwstL/HKpYQcdBh87yRf3I+6X0IhBKTogGTYMaLF+fNPKQ==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'5', N'BmpoijQpWQDlokEkjqbl1cWd8nN52t7Uw5tmhWvryES6fWEEGl5Cdx7ZlGlaFgM=', N'J0TQfeLMQUI+Hb+yESIDM3D7FkN+qPv7XnScLI/fj0nzdxPjZw==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'6', N'9niaAAIbU4J+ZWByW5kBWJBRCwoEjUb/gEIRLPBg13YhTb+ARNBq3wpa17EZUkI=', N'UdrbPAf3tXyOQqC7sQZf+lj15Zzs7+dOTR72yfeCWmtc3XQu2w==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'7', N'jTMvZbLgG1/pjST0RkOaQ/NYSZv9lpqvtZtK8le7whys+B/PxIc9hOPrFnursLM=', N'2q9KhxqVaOVxDDd9wnhHm6m37YE/IK8msJDTnOolyFBO0B5ESg==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'8', N'MxEEtk1majyrmxmb2nyxFZLQOKS4ZmflFoKXHLMJVaKPj921JmVd6RMY4LFlmGY=', N'7HxKWmExv4FiODYOD06nVckRu0fU4secYSj98BbrtTew5VgRdA==')
INSERT [dbo].[SinhVien] ([maSinhVien], [tenSinhVien], [lop]) VALUES (N'9', N'OU21WkRkaMPIuuXzDLAOFkCHhAv6r465byqkbYHrISTI9b+o4x0Xqb10UR6rLso=', N'wVJhvygtRiLlYf/TrgMPsvaE9RNECk0Y8QchuiusbTurP2ogoQ==')
GO
ALTER TABLE [dbo].[Diem]  WITH CHECK ADD  CONSTRAINT [FK__Diem__maMonHoc__3C69FB99] FOREIGN KEY([maMonHoc])
REFERENCES [dbo].[MonHoc] ([maMonHoc])
GO
ALTER TABLE [dbo].[Diem] CHECK CONSTRAINT [FK__Diem__maMonHoc__3C69FB99]
GO
ALTER TABLE [dbo].[Diem]  WITH CHECK ADD  CONSTRAINT [FK__Diem__maSinhVien__3B75D760] FOREIGN KEY([maSinhVien])
REFERENCES [dbo].[SinhVien] ([maSinhVien])
GO
ALTER TABLE [dbo].[Diem] CHECK CONSTRAINT [FK__Diem__maSinhVien__3B75D760]
GO
USE [master]
GO
ALTER DATABASE [QLSV] SET  READ_WRITE 
GO
