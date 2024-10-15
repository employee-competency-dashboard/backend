import { DetailedHTMLProps, HTMLAttributes } from 'react';
// import { typeAboutTeamProps } from '@/source/features/about-team/types';

export interface typeWelcomeInfoProps
  extends DetailedHTMLProps<HTMLAttributes<HTMLElement>, HTMLElement> {
  // welcomeData: typeAboutTeamProps['welcomeData'];
  welcomeData: {
    teamName: string;
    description: string;
    tags: {
      title: string;
    }[];
    managers: {
      jobPosition: string;
      photo: string | null;
      firstName: string;
      lastName: string;
    }[];
    links: {
      name: string;
      title: string;
      link: string;
    }[];
  };
  importantData: {
    item: string;
  }[];
  editProfileTeam: () => void;
}
